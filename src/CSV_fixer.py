import csv
import os

for x in ['16', '32', '64']:
    for y in ['0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9']:
        for z in ['']:
            folder_name = f'results/scenarioB3_N{x}_Pformulated_Cformulated1.000_B{y}_T15000_annealer'
            fixed_folder_name = f'results/scenarioB3_N{x}_Pformulated_Cformulated1.000_B{y}_T15000_annealer_FIXED'
            # Check if folder exists and creates if not
            if not os.path.exists(fixed_folder_name):
                os.makedirs(fixed_folder_name)

            for filename in os.listdir(folder_name):
                if '.csv' in filename:
                    with open(folder_name + '/' + filename, 'r') as infile, open(fixed_folder_name + '/' + filename, 'w', newline='') as outfile:
                        # output dict needs a list for new column ordering
                        if x == '64':
                            fieldnames = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','chain_break_fraction','energy','num_occurrences']
                        elif x == '32':
                            fieldnames = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','chain_break_fraction','energy','num_occurrences']
                        elif x == '16':
                            fieldnames = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','chain_break_fraction','energy','num_occurrences']
                        else:
                            fieldnames = ['0','1','2','3','4','5','6','7','chain_break_fraction','energy','num_occurrences']
                        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                        # reorder the header first
                        writer.writeheader()
                        for row in csv.DictReader(infile):
                            # writes the reordered rows to the new file
                            writer.writerow(row)