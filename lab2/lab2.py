from stb import STB

key = 'RTYBHncnfeicnjiujUFCTYU234huU-sQ'

if __name__ == '__main__':
    stb = STB(key)
    data = input('Input Text: ')
    print()
    

    print('Шифрование в режиме простой замены')
    encrypted = stb.encrypt_simple_substitute(data)
    print("Encrypted ", encrypted)
    decrypted = stb.decrypt_simple_substitute(encrypted)
    print("Decrypted ", decrypted)

    print('\nШифрование в режиме сцепления блоков')
    sync = '12345678abcdefgh'

    encrypted = stb.encrypt_clutch_blocks(data, sync)
    print("Encrypted ", encrypted)
    decrypted = stb.decrypt_clutch_blocks(encrypted, sync)
    print("Decrypted ", decrypted)

    print('\nШифрование в режиме гаммирования с обратной связью')
    sync = '12345678abcdefgh'

    encrypted = stb.encrypt_gamming(data, sync)
    print("Encrypted ", encrypted)
    decrypted = stb.decrypt_gamma_with_feedback(encrypted, sync)
    print("Decrypted ", decrypted)
