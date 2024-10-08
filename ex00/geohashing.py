import sys
import antigravity

def main():
    if len(sys.argv) == 4:
        try:
            latitude = float(sys.argv[1])
        except ValueError:
            return print("Error: latitude required type: float")
        
        try:
            longitude = float(sys.argv[2])
        except ValueError:
            return print("Error: longitude required type: float")
        
        datedow = sys.argv[3]  # No need to try-except, as argv elements are always strings
        antigravity.geohash(latitude, longitude, datedow.encode('utf-8'))
        
        geohash = f"{latitude},{longitude},{datedow}"
        print(f"Generated Geohash: {geohash}")
    else:
        print("Error: 3 arguments required (latitude, longitude, datedow)")

if __name__ == '__main__':
    main()
