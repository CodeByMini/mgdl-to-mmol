from datetime import datetime


def parser():
    f = open("list.csv")

    dates = []
    values = []
    days = []
    for line in f:
        item = line.split(";")
        dates.append(datetime.strptime(item[0], "%m/%d/%y %H:%M"))
        values.append(float(item[1]) / 18)

    # writer = StringIO()
    outfile = open("parsed.csv", "w")

    firstrow = "Glukosuppgifter,Skapat den,,Skapat av,\n"
    secondrow = "Enhet,Serienummer,Enhetens tidsstämpel,Registertyp,Historiskt glukosvärde mmol/L,Skanna glukosvärde mmol/L,Icke-numeriskt snabbverkande insulin,Snabbverkande insulin (enheter),Icke-numerisk mat,Kolhydrater (gram),Kolhydrater (portioner),Icke-numeriskt långtidsverkande insulin,Långtidsverkande insulin (enheter),Anteckningar,Glukossticka mmol/L,Keton mmol/L,Måltidsinsulin (enheter),Korrigeringsinsulin (enheter),Användarändrat insulin (enheter)\n"

    serial_str = "5828D090-51AF-4EFB-A47F-9CC06259EA49"
    outfile.write(firstrow)
    outfile.write(secondrow)
    for i in range(len(dates)):
        print(dates[i])
        date = dates[i].strftime("%m-%d-%Y %H:%M")
        value = str(values[i])

        row = (
            "Freestyle Libre,"
            + serial_str
            + ","
            + date
            + ',0,"'
            + value
            + '",,,'
            + ",,,,,,,,,,,\n"
        )

        outfile.write(row)

    outfile.close()
    print(days)


if __name__ == "__main__":
    parser()
