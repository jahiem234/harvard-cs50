import csv
import sys


def main():
    # Check command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python dna.py database.csv sequence.txt")
        sys.exit(1)

    # Load database
    with open(sys.argv[1], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        database = list(reader)
        str_list = reader.fieldnames[1:]

    # Load DNA sequence
    with open(sys.argv[2], 'r') as seqfile:
        dna_sequence = seqfile.read()

    # Count STRs
    str_counts = {}
    for STR in str_list:
        str_counts[STR] = longest_match(dna_sequence, STR)

    # Compare
    for person in database:
        match = all(int(person[STR]) == str_counts[STR] for STR in str_list)
        if match:
            print(person["name"])
            return

    print("No match")


def longest_match(sequence, subsequence):
    longest_run = 0
    subseq_len = len(subsequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        count = 0
        while sequence[i + count * subseq_len: i + (count + 1) * subseq_len] == subsequence:
            count += 1
        longest_run = max(longest_run, count)

    return longest_run


if __name__ == "__main__":
    main()
