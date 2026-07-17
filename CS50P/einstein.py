def main():
    print("EINSTEIN'S ENERGY CALCULATOR")
    print("════════════════════════════")
    
    m = int(input("Mass (kg): "))
    
    # Calculate energy
    c = 300000000
    e = m * (c ** 2)
    
    print(f"Energy: {e:,} Joules\n")

main()