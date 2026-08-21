
def read_files():
    with open('receipts/2026-05-30 11:27_59941.txt', 'r') as f:
        result = f.read()
    return result
def main():
    print(read_files())

if __name__ == "__main__":
    main()