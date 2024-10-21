import struct

def convert_endian(input_file, output_file):
    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        while True:
            # Lire 4 octets (32 bits)
            data = f_in.read(4)

            # Si la taille de data est inférieure à 4, on a atteint la fin du fichier
            if len(data) < 4:
                break

            # Convertir les données de little-endian à entier
            little_endian_value = struct.unpack('<I', data)[0]

            # Convertir en big-endian
            big_endian_value = struct.pack('>I', little_endian_value)

            # Écrire les données converties dans le fichier de sortie
            f_out.write(big_endian_value)

# Exemple d'utilisation
input_file = 'challengefile'
output_file = 'fichier_big_endian'
convert_endian(input_file, output_file)
