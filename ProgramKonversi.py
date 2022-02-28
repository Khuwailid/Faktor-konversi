#Hallo semalat datang, semoga berguna
#program konversi
#Vioneles Asterna
print("\nSELAMAT DATANG DI PROGRAM KONVERSI")
print("Silahkan pilih dimensi yang akan di konversi")
print("1. Suhu\n2. Panjang \n3. Volume\n4. Berat\n5. Tekanan\n6. Massa Jenis")
    
while True:
    pilihan=(int(input("Masukkan nomor pilihan anda:\n")))
    if pilihan == 1:
     print(" PROGRAM KONVERSI TEMPERATURE")
     print("1. Celsius\n2. Fahreiheit\n3. Kelvin\n4. Reamur")

     while True:
        suhu=(int(input("Masukkan nomor temperatur yang akan dikonversi:\n")))
        if suhu == 1:
            print("Konversi Celsius")
            
            #celsius ke reamur
            celsius = float(input ('Masukkan suhu dalam Celsius\n'))
            print("suhu adalah",celsius, "°Celsius")

            reamur = (4/5) *celsius
            print("Suhu dalam Reamur=", reamur, "°Reamur")

            fahrenheit = (9/5)*(celsius+32)
            print("Suhu dalam fahrenheit=", fahrenheit, "°Fahrenheit")

            kelvin = 273+celsius
            print("Suhu dalam kelvin=", kelvin, "°Kelvin")
        elif suhu == 2:
                print("Konversi Fahrenheit")

                #conversi fahrenheit
                fahrenheit = float(input('Masukkan suhu dalam Fahrenheit =\n'))
                print("suhu adalah",fahrenheit, "°Fahrenheit")

                #fahrenheit ke celsius
                celsius = (5/9)*(fahrenheit-32)
                print("Suhu dalam celsius=", celsius, "°Celsius")

                #fahrenheit ke reamur
                reamur = (4/9)*(fahrenheit-32)
                print("Suhu dalam reamur=", reamur, "°Reamur")

                #fahrenheit ke kelvin
                kelvin = celsius+273
                print("Suhu dalam kelvin=", kelvin, "°Kelvin")
        elif suhu == 3:
                print("Konversi Kelvin")

                #conversi Kelvin
                kelvin = float(input('Masukkan suhu dalam Kelvin =\n'))
                print("suhu adalah",kelvin, "°Kelvin")

                #Kelvin ke celsius
                celsius = kelvin-273
                print("Suhu dalam celsius=", celsius,"°Celsius")

                #kelvin ke reamur
                reamur = (5/4)*celsius
                print("Suhu dalam reamur=", reamur, "°Reamur")

                #kelvin ke fahrenheit
                fahrenheit = (9/5)*(celsius+32)
                print("Suhu dalam fahrenheit=", fahrenheit, "°Fahrenheit")
        elif suhu == 4:
                print("Konversi Reamur")

                #conversi Kelvin
                reamur = float(input('Masukkan suhu dalam Reamur =\n'))
                print("suhu adalah",reamur, "°Reamur")

                #Kelvin ke celsius
                celsius = (5/4)*reamur
                print("Suhu dalam celsius=", celsius,"°Celsius")

                #reamur ke kelvin
                kelvin = celsius+273
                print("Suhu dalam kelvin=", kelvin, "°Kelvin")

                #reamur ke fahrenheit
                fahrenheit = (9/5)*(celsius+32)
                print("Suhu dalam fahrenheit=", fahrenheit, "°Fahrenheit")
        else:
                print("Hanya tersedia 1 sampai 4")
    elif pilihan == 2:
     print("\n PROGRAM KONVERSI PANJANG\n")
     print("1. nm\n2. mikron\n3. cm\n4. m\n5. inch\n6. foot\n7. yard\n8. Mile")

     while True:
        Panjang=(int(input("Masukkan nomor Panjang yang akan dikonversi:\n")))
        if Panjang == 1:
         
            print("Konversi nm")

            nm = float(input ('Masukkan Panjang dalam nm\n'))
            print("Panjang adalah",nm, "nm")

            mikron = 1/1000 *nm
            print("Panjang dalam mikron=", mikron, "mikron")

            cm = 10000000 * nm
            print("Panjang dalam cm=", cm, "cm")

            m = 1000 * cm  
            print("Panjang dalam m=", m, "m")

            inch = 25400000 * nm
            print("Panjang dalam inch=", inch, "inch")

            foot = 304800000 * nm
            print("Panjang dalam foot=", foot, "foot")

            yard = 1.09361*(10**9) * nm
            print("Panjang dalam yard=", yard, "yard")

            mile = 6.21371*(10**13) * nm
            print("Panjang dalam mile=", mile, "mile")

        elif Panjang == 2:
                    print("Konversi mikron")
                    
                    mikron = float(input ('Masukkan Panjang dalam mikron\n'))
                    print("Panjang adalah",mikron, "mikron")

                    nm = 1000 *nm
                    print("Panjang dalam nm=", nm, "nm")

                    cm = 1/1000000 * mikron
                    print("Panjang dalam cm=", cm, "cm")

                    m = 1/1000 * cm  
                    print("Panjang dalam m=", m, "m")

                    inch = 2.54  * cm
                    print("Panjang dalam inch=", inch, "inch")

                    foot = 30.48  * cm
                    print("Panjang dalam foot=", foot, "foot")

                    yard = 91.44  * cm
                    print("Panjang dalam yard=", yard, "yard")

                    mile = 1609.344  * m
                    print("Panjang dalam mile=", mile, "mile")
        elif Panjang == 3:
                    print("Konversi cm")
                    
                    cm = float(input ('Masukkan Panjang dalam cm\n'))
                    print("Panjang adalah",cm, "cm")

                    nm = 10000000 * cm
                    print("Panjang dalam nm=", nm, "nm")

                    mikron = 10000 *cm
                    print("Panjang dalam mikron=", mikron, "mikron")

                    m = 1/1000 * cm 
                    print("Panjang dalam m=", m, "m")

                    inch = 2.54  * cm
                    print("Panjang dalam inch=", inch, "inch")

                    foot = 30.48  * cm
                    print("Panjang dalam foot=", foot, "foot")

                    yard = 91.44  * cm
                    print("Panjang dalam yard=", yard, "yard")

                    mile = 1609.344  * m
                    print("Panjang dalam mile=", mile, "mile")
        elif Panjang == 4:
                    print("Konversi m")
                    
                    m = float(input ('Masukkan Panjang dalam m\n'))
                    print("Panjang adalah",m, "m")

                    nm = (10**9) * m  
                    print("Panjang dalanm n=", nm, "nm")

                    mikron = (10**6) *m
                    print("Panjang dalam mikron=", mikron, "mikron")

                    cm = 100 * m
                    print("Panjang dalam cm=", cm, "cm")

                    inch = 39.37008 * m
                    print("Panjang dalam inch=", inch, "inch")

                    foot = 3.28084  * m
                    print("Panjang dalam foot=", foot, "foot")

                    yard = 1.09361  * m
                    print("Panjang dalam yard=", yard, "yard")

                    mile = 0.00062  * m
                    print("Panjang dalam mile=", mile, "mile")
        elif Panjang == 5:
                    print("Konversi inch")
                    
                    inch = float(input ('Masukkan Panjang dalam inch\n'))
                    print("Panjang adalah",inch, "inch")

                    nm = 25400000 * inch
                    print("Panjang dalam nm=", nm, "nm")

                    mikron = 25400 * inch
                    print("Panjang dalam mikron=", mikron, "mikron")

                    cm = 1/10000 * mikron
                    print("Panjang dalam cm=", cm, "cm")

                    m = 1/100 * cm  
                    print("Panjang dalam m=", m, "m")

                    foot = 30.48  * cm
                    print("Panjang dalam foot=", foot, "foot")

                    yard = 1.09361  * m
                    print("Panjang dalam yard=", yard, "yard")

                    mile = 1609.344  * m
                    print("Panjang dalam mile=", mile, "mile")  
        elif Panjang == 6:
                    print("Konversi foot")
                    
                    foot = float(input ('Masukkan Panjang dalam foot\n'))
                    print("Panjang adalah",foot, "foot")

                    nm = 304800000 * nm
                    print("Panjang dalam nm=", nm, "nm")

                    mikron = 1/1000 *nm
                    print("Panjang dalam mikron=", mikron, "mikron")

                    cm = 1/10000 * mikron
                    print("Panjang dalam cm=", cm, "cm")

                    m = 1/100 * cm  
                    print("Panjang dalam m=", m, "m")

                    inch = 2.54  * cm
                    print("Panjang dalam inch=", inch, "inch")

                    yard = 1.09361  * m
                    print("Panjang dalam yard=", yard, "yard")

                    mile = 1609.344  * m
                    print("Panjang dalam mile=", mile, "mile")
        elif Panjang == 7:
                    print("Konversi yard")
                    
                    yard = float(input ('Masukkan Panjang dalam yard\n'))
                    print("Panjang adalah",yard, "yard")

                    nm = 914400000 * yard
                    print("Panjang dalam nm=", nm, "nm")

                    mikron = 1/1000 *yard
                    print("Panjang dalam mikron=", mikron, "mikron")

                    cm = 1/10000 * mikron
                    print("Panjang dalam cm=", cm, "cm")

                    m = 1/100 * cm   
                    print("Panjang dalam m=", m, "m")

                    inch = 2.54  * cm
                    print("Panjang dalam inch=", inch, "inch")

                    foot = 30.48  * cm
                    print("Panjang dalam foot=", foot, "foot")

                    mile = 1609.344  * m
                    print("Panjang dalam mile=", mile, "mile")
        elif Panjang == 8:    
                    print("Konversi mile")
                    
                    mile = float(input ('Masukkan Panjang dalam mile\n'))
                    print("Panjang adalah",mile, "mile")

                    mikron = 1609344000 *mile
                    print("Panjang dalam mikron=", mikron, "mikron")

                    cm = 1/10000 * mikron
                    print("Panjang dalam cm=", cm, "cm")
                    
                    m = 1/100 * cm  
                    print("Panjang dalam m=", m, "m")

                    inch = 2.54  * cm
                    print("Panjang dalam inch=", inch, "inch")

                    foot = 30.48  * cm
                    print("Panjang dalam foot=", foot, "foot")

                    yard = 1.09361  * m
                    print("Panjang dalam yard=", yard, "yard")

        else:
                    print("Hanya tersedia 1 sampai 8")
    if pilihan == 3:
     print("\n PROGRAM KONVERSI VOLUME\n")
     print("1. mm³\n2. cm³\n3. m³\n4. inch³\n5. foot³\n6. liter")

     while True:
         Volume=(int(input("Masukkan nomor Volume yang akan dikonversi:\n")))
         if Volume == 1:
          print("Konversi mm³")
          
          mmkubik = float(input ('Masukkan Volume dalam mm³\n'))
          print("Volume adalah",mmkubik, "mm³")

          cmkubik = 1/1000 *mmkubik
          print("Volume dalam cm³=", cmkubik, "cm³")

          mkubik = 1/1000000  * mmkubik
          print("Volume dalam m³=", mkubik, "m³")

          inchkubik = 0.06102  * mmkubik  
          print("Volume dalam inch³=", inchkubik, "inch³")

          footkubik = 0.00004  * mmkubik
          print("Volume dalam foot³=", footkubik, "foot³")

          liter = 0.000001  * mmkubik
          print("Volume dalam liter=", liter, "liter")
         elif Volume == 2:
             print("Konversi cm³")

             cmkubik = float(input('Masukkan Volume dalam cm³ =\n'))
             print("Volume adalah",cmkubik, "cm³")

             mmkubuik = 1000 * cmkubik
             print("Volume dalam mg=", mmkubuik, "mg")

             mkubuik = 1/1000000 * cmkubik
             print("Volume dalam m³=", mkubuik, "m³")

             inchkubik = 0.06102  * cmkubik
             print("Volume dalam inch³=", inchkubik, "inch³")

             footkubik = 0.0000353147 * cmkubik
             print("Volume dalam foot³=", footkubik,"foot³")

             liter = 0.001  * cmkubik
             print("Volume dalam liter=", liter, "liter")
         elif Volume == 3:
             print("Konversi m³")

             mkubik = float(input('Masukkan Volume dalam m³ =\n'))
             print("Volume adalah",mkubik, "m³")

             mmkubik = 1.000000000 * mkubik
             print("Volume dalam mm³=", mmkubik,"mm³")

             cmkubik = 1000000 * mkubik
             print("Volume dalam cm³=", cmkubik, "cm³")

             inchkubik = 61023.76  * mkubik 
             print("Volume dalam inch³=", inchkubik, "inch³")

             footkubik = 35.31468  * mkubik 
             print("Volume dalam foot³=", footkubik, "foot³")

             liter = 1000 * mkubik 
             print("Volume dalam liter=", liter, "liter")
         elif Volume == 4:
             print("Konversi inch³")

             inchkubik = float(input('Masukkan Volume dalam inch³ =\n'))
             print("Volume adalah",inchkubik, "inch³")

             mmkubik = 16387.05973  * inchkubik 
             print("Volume dalam mm³=", mmkubik,"mm³")

             cmkubik = 16.38706  * inchkubik
             print("Volume dalam cm³=", cmkubik, "cm³")

             mkubik = 1/1000000  * cmkubik 
             print("Volume dalam m³=", mkubik, "m³")

             footkubik = 0,.0005787037  * inchkubik 
             print("Volume dalam foot³=", footkubik, "foot³")

             liter = 0.01639   * inchkubik
             print("Volume dalam liter=", liter, "liter")
         elif Volume == 5:
             print("Konversi foot³")

             footkubik = float(input('Masukkan Volume dalam foot³ =\n'))
             print("Volume adalah",footkubik, "foot³")

             mmkubik = 2.8316835945*(10**7)   * footkubik 
             print("Volume dalam mm³=", mmkubik,"mm³")

             cmkubik = 1/1000  * mmkubik
             print("Volume dalam cm³=", cmkubik, "cm³")

             mkubik = 1/1000000  * cmkubik 
             print("Volume dalam m³=", mkubik, "m³")

             inchkubik = 1727.9998   * footkubik 
             print("Volume dalam inch³=", inchkubik, "inch³")

             liter = 28.31684  * footkubik 
             print("Volume dalam liter=", liter, "liter")  
         elif Volume == 6:
             print("Konversi liter")

             liter = float(input('Masukkan Volume dalam liter =\n'))
             print("Volume adalah",liter, "liter")

             mmkubik = 1000000   * liter 
             print("Volume dalam mm³=", mmkubik,"mm³")

             cmkubik = (10**3) * liter
             print("Volume dalam cm³=", cmkubik, "cm³")

             mkubik = 0.001  * liter 
             print("Volume dalam m³=", mkubik, "m³")

             inchkubik = 61.02376  * liter 
             print("Volume dalam inch³=", inchkubik, "inch³")      

             footkubik = 0.03531   * liter 
             print("Volume dalam foot³=", footkubik, "foot³")
         else:
             print("Hanya tersedia 1 sampai 6")
    if pilihan == 4:
     print("\n PROGRAM KONVERSI BERAT\n")
     print("1. mg\n2. Gram\n3. kg\n4. pound\n5. Ons\n6. Ton")

     while True:
         Berat=(int(input("Masukkan nomor berat yang akan dikonversi:\n")))
         if Berat == 1:
          print("Konversi mg")
          
          #celsius ke reamur
          mg = float(input ('Masukkan Berat dalam mg\n'))
          print("Berat adalah",mg, "mg")

          gram = 1/1000 *mg
          print("Berat dalam gram=", gram, "gram")

          kg = 1/1000000 * mg
          print("Berat dalam kg=", kg, "kg")

          pound = (2.2*(1/1000000))*mg
          print("Berat dalam pound=", pound, "pound")

          ons = (3.53*(1/100000)) * mg
          print("Berat dalam ons=", ons, "ons")

          Ton = 1/10**9 * mg
          print("Berat dalam Ton=", Ton, "Ton")
         elif Berat == 2:
             print("Konversi gram")

             gram = float(input('Masukkan Berat dalam gram =\n'))
             print("Berat adalah",gram, "gram")

             mg = 1000 * gram
             print("Berat dalam mg=", mg, "mg")

             kg = 1/1000 * gram
             print("Berat dalam kg=", kg, "kg")

             pound = (2.2*(1/1000))*gram
             print("Berat dalam pound=", pound, "pound")

             ons = 0.04 * gram
             print("Berat dalam ons=", ons, "ons")

             ton = 1/1000000 * gram
             print("Berat dalam ton=", ton, "ton")
         elif Berat == 3:
             print("Konversi kg")

             kg = float(input('Masukkan Berat dalam kg =\n'))
             print("Berat adalah",kg, "kg")

             mg = 1000000 * kg
             print("Berat dalam mg=", mg,"mg")

             gram = 1000 * kg
             print("Berat dalam gram=", gram, "gram")

             pound = 2.204623 * kg 
             print("Berat dalam pound=", pound, "pound")

             ons = 0.00004 * kg 
             print("Berat dalam ons=", ons, "ons")

             ton = 1/1000 * kg 
             print("Berat dalam ton=", ton, "ton")
         elif Berat == 4:
             print("Konversi pound")

             pound = float(input('Masukkan Berat dalam pound =\n'))
             print("Berat adalah",pound, "pound")

             mg = 453592.37  * pound 
             print("Berat dalam mg=", mg,"mg")

             gram = 1/1000 * mg
             print("Berat dalam gram=", gram, "gram")

             kg = 1/1000 * gram 
             print("Berat dalam kg=", kg, "kg")

             ons = 16 * pound 
             print("Berat dalam ons=", ons, "ons")

             ton = 1000  * kg 
             print("Berat dalam ton=", ton, "ton")
         elif Berat == 5:
             print("Konversi ons")

             ons = float(input('Masukkan Berat dalam ons =\n'))
             print("Berat adalah",ons, "ons")

             mg = 28349.52313   * ons 
             print("Berat dalam mg=", mg,"mg")

             gram = 28.34952  * ons
             print("Berat dalam gram=", gram, "gram")

             kg = 0.02835  * ons 
             print("Berat dalam kg=", kg, "kg")

             pound = 0.0625  * ons 
             print("Berat dalam pound=", pound, "pound")

             ton = 1000 * kg 
             print("Berat dalam ton=", ton, "ton")  
         elif Berat == 6:
             print("Konversi ton")

             ton = float(input('Masukkan Berat dalam ton =\n'))
             print("Berat adalah",ton, "ton")

             mg = 10**9  * ton 
             print("Berat dalam mg=", mg,"mg")

             gram = 10**6 * ton
             print("Berat dalam gram=", gram, "gram")

             kg = 1000 * ton 
             print("Berat dalam kg=", kg, "kg")

             pound = 2.2046226218*1000 * ton 
             print("Berat dalam pound=", pound, "pound")      

             ons = 3.527396195*10000  * ton 
             print("Berat dalam ons=", ons, "ons")
         else:
             print("Hanya tersedia 1 sampai 5")
    if pilihan == 5:
     print("\n PROGRAM KONVERSI TEKANAN\n")
     print("1. Atm\n2. Bar\n3. Pascal\n4. Kilopascal\n5. mmHg\n6. psi")

     while True:
         Tekanan=(int(input("Masukkan nomor tekanan yang akan dikonversi:\n")))
         if Tekanan == 1:
          print("Konversi Atm")
          
          #Atm ke satuan lain
          Atm = float(input ('Masukkan tekanan dalam satuan Atm\n'))
          print("Tekanan adalah",Atm, "Atm")

          Bar = 1.0132499658 *Atm
          print("Tekanan dalam Bar=", Bar, "Bar")

          Pascal = 1.0132499658*100000 * Atm
          print("Tekanan dalam Pascal=", Pascal, "Pascal")

          Kilopascal = 1/1000 * Pascal
          print("Tekanan dalam Kilopascal=", Kilopascal, "Kilopascal")

          mmHg = 2.9921342418*10 * Atm
          print("Tekanan dalam mmHg=", mmHg, "mmHg")

          psi = 14,69594 * Atm
          print("Tekanan dalam psi=", psi, "psi")
         elif Tekanan == 2:
             print("Konversi Bar")

             Bar = float(input('Masukkan Tekanan dalam Bar =\n'))
             print("Tekanan adalah",Bar, "Bar")

             Atm = 0.9869233 * Bar
             print("Tekanan dalam Atm=", Atm, "Atm")
            
             Pascal = 100000 * Bar
             print("Tekanan dalam Pascal=", Pascal, "Pascal")

             Kilopascal = 1/1000 * Pascal
             print("Tekanan dalam Kilopascal=", Kilopascal, "Kilopascal")
             
             mmHg =750.0638  * Bar
             print("Tekanan dalam mmHg=", mmHg, "mmHg")

             psi = 14.50377  * Bar
             print("Tekanan dalam psi=", psi, "psi")
         elif Tekanan == 3:
             print("Konversi Pascal")

             Pascal = float(input('Masukkan Tekanan dalam Pascal =\n'))
             print("Tekanan adalah",Pascal, "Pascal")

             Atm = 0.0000098692  * Pascal
             print("Tekanan dalam Atm=", Atm, "Atm")

             Bar = 0.00001   * Pascal
             print("Tekanan dalam Bar=", Bar, "Bar")
            
             KiloPascal = 1/1000 * Pascal
             print("Tekanan dalam Pascal=", Pascal, "Pascal")
             
             mmHg =0.007500638   * Pascal
             print("Tekanan dalam mmHg=", mmHg, "mmHg")

             psi =0.0001450377  * Pascal
             print("Tekanan dalam psi=", psi, "psi")    
         elif Tekanan == 4:
             print("Konversi Kilopascal")

             Kilopascal = float(input('Masukkan Tekanan dalam Kilopascal =\n'))
             print("Tekanan adalah",Kilopascal, "Kilopascal")

             Atm = 0.009869 * Kilopascal
             print("Tekanan dalam Atm=", Atm,"Atm")

             Bar = 1/100  * Kilopascal
             print("Tekanan dalam Bar=", Bar, "Bar")

             Pascal = 1000 * Kilopascal
             print("Tekanan dalam Pascal=", Pascal, "Pascal")

             mmHg = 7.500638 * Kilopascal
             print(f'Tekanan dalam mmHg= {mmHg} mmHg')

             psi = 0.1450377 * Kilopascal
             print(f'Tekanan dalam psi = {psi} psi')
         elif Tekanan == 5:
             print("Konversi mmHg")

             mmHg = float(input('Masukkan Tekanan dalam mmHg =\n'))
             print("Tekanan adalah",mmHg, "mmHg")

             Atm = 0.0013157858*mmHg
             print("Tekanan dalam Atm=", Atm,"Atm")

             Bar = 0.0013332199 * mmHg
             print("Tekanan dalam Bar=", Bar, "Bar")

             Pascal = 1.3332199208*(10**2)  * mmHg
             print("Tekanan dalam Pascal=", Pascal, "Pascal")

             KiloPascal = 1/1000 * Pascal
             print("Tekanan dalam KiloPascal=", KiloPascal, "KiloPascal")

             psi = 0.0193367151 * mmHg 
             print("Tekanan dalam psi=", psi, "psi")
         elif Tekanan == 6:
             print("Konversi psi")

             psi = float(input('Masukkan Tekanan dalam psi =\n'))
             print("Tekanan adalah",psi, "psi")

             Atm = 0.0680459839 *psi
             print("Tekanan dalam Atm=", Atm,"Atm")

             Bar = 0.0689475909  * psi
             print("Tekanan dalam Bar=", Bar, "Bar")

             Pascal =6.8947590868*103 * psi
             print("Tekanan dalam Pascal=", Pascal, "Pascal")

             KiloPascal = 1/1000  * Pascal
             print("Tekanan dalam KiloPascal=", KiloPascal, "KiloPascal")

             mmHg = 0.01934  * mmHg 
             print("Tekanan dalam mmHg=", mmHg, "mmHg")    
         else:
             print("Pilihan tidak tersedia, hanya dapat memilih 1 sampai 6")
    if pilihan == 6:
     print("\n PROGRAM KONVERSI massa jenis\n")
     print("1. kg/m³\n2. g/cm³\n3. lb/ft³")

     while True:
         massajenis=(int(input("Masukkan nomor massa jenis yang akan dikonversi:\n")))
         if massajenis == 1:
          print("Konversi kg/m³")
          
          kgperm = float(input("Masukkan massa jenis dalam kg/m³:\n"))
          print("massa jenis adalah",kgperm, "kg/m³")

          gpercm = 0.001  *kgperm
          print("massa jenis dalam g/cm³=", gpercm, "g/cm³")

          lbperft = 0.06243  * kgperm
          print("massa jenis dalam lb/ft³=", lbperft, "lb/ft³")

         elif massajenis == 2:
             print("Konversi g/cm³")

             gpercm = float(input('Masukkan massa jenis dalam g/cm³ =\n'))
             print("massa jenis adalah",gpercm, "g/cm³")

             kgperm = 1000 * gpercm
             print("massa jenis dalam kg/m³=", kgperm, "kg/m³")

             lbperft = 62.42796  * gpercm
             print("massa jenis dalam lb/ft³=", lbperft, "lb/ft³")

         elif massajenis == 3:
             print("Konversi lb/ft³")

             lbperft = float(input('Masukkan massa jenis dalam lb/ft³ =\n'))
             print("massa jenis adalah",lbperft, "lb/ft³")

             kgpercm = 16.01846  * lbperft
             print("massa jenis dalam mg=", kgpercm,"lb/ft³")

             gpercm = 0.01602 * lbperft
             print("massa jenis dalam gram=", gpercm, "gram")
         else:
             print("Hanya tersedia 1 sampai 3")    
    else:
        print ("Pilihan tidak tersedia, silahkan pilih 1-6")                     