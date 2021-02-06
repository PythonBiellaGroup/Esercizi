def americana(metri):
    conversions = dict()
    conversions["miglia"] = metri / 1609.344
    conversions["piedi"] = metri * 3.280840
    conversions["pollici"] = metri * 39.37008
    conversions["iarde"] = metri * 1.093613

    print(f"{metri} metri corrispondono a:")
    for key, value in conversions.items():
        print(f"{key}: {value}")