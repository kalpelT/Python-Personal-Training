from Bio import SeqIO

gb_file_path = 'C:/Users/Example'
fasta_file_path = 'C:/Users/Example'
combined_fasta_file_path = 'C:/Users/Example'


with open(gb_file_path, 'r') as gb_file:
    gb_records = SeqIO.parse(gb_file, 'genbank')


    with open(combined_fasta_file_path, 'w') as combined_file:
        for record in gb_records:
            SeqIO.write(record, combined_file, 'fasta')


with open(fasta_file_path, 'r') as fasta_file:
    fasta_records = SeqIO.parse(fasta_file, 'fasta')


    with open(combined_fasta_file_path, 'a') as combined_file:
        SeqIO.write(fasta_records, combined_file, 'fasta')

print(f"Birleştirilmiş FASTA dosyası oluşturuldu: {combined_fasta_file_path}")