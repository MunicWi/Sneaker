a = [] 
p = [] 
while True:
    s = input('-------------------------\n   Sneaker North Shop\n-------------------------\n\n       Shock Price!!!!!\n\nNike sale 20% Adidas sale 30% Reebox sale 70%\n\n1)Nike   [n]\n2)Adidas [a]\n3)Reebok [r]\n4)Vans   [v]\n5)Exit   [x]\nเช็คยอด   [b]\n')
    s = s.lower()
    if s=='n': 
        ni = input('*************Nike*************\n1)Nike Air Force 1         3,360 B\n2)Nike Jordan x Off-white  78,400 B\n3)Air Jordan 1 Mid         3,360 B\n') 
        if ni=='1': 
            t = ('Nike Air Force 1            4,200 B        20%      3,360 B') 
            pt = 4200-(4200*0.2) 
            print(input('Nike Air Force 1            4,200 B   ลด 20%')) 
            a.append(t) 
            p.append(pt) 
        elif ni=='2': 
            f = ('Nike Jordan x Off-white     98,000 B       20%      78,400 B')
            pf = 98000-(98000*0.2) 
            print(input('Nike Jordan x Off-white     98,000 B     ลด 20%'))
            a.append(f)
            p.append(pf)
        elif ni=='3':
            m = ('Nike Air Jordan 1 Mid 1     4,200 B        20%      3,360 B')
            pm = 4200-(4200*0.2)
            print(input('Nike Air Jordan 1 Mid 1     4,200 B      ลด 20%'))
            a.append(m)
            p.append(pm)
        else:
            c = input('กรุณากด Enter เพื่อเริ่มรายการใหม่')
             
    if s=='a':
        ads = input('*************Adidas*************\n1)Adidas Ultraboost      4,550 B\n2)Adidas NMD          2,490 B\n3)Adidas Stan Smith   1,960 B\n')
        if ads=='1':
            au = ('Adidas Ultraboost           6,500 B        30%      4,550 B')
            pau = 6500-(6500*0.3)
            print(input('Adidas Ultraboost          6,500 B     ลด 30%'))
            a.append(au)
            p.append(pau)
        elif ads=='2':
            of = ('Adidas NMD                  4,200 B        30%      2,490 B')
            pof = 4200-(4200*0.3)
            print(input('Adidas NMD                 4,200 B     ลด 30%'))
            a.append(of)
            p.append(pof)
        elif ads=='3':
            jm = ('Adidas Stan Smith           2,800 B        30%      1,960 B')
            pjm = 2800-(2800*0.3)
            print(input('Adidas Stan Smith          2,800 B     ลด 30%'))
            a.append(jm)
            p.append(pjm)
        else:
            c = input('กรุณากด Enter เพื่อเริ่มรายการใหม่')
    if s=='r':
        ads = input('*************Reebok*************\n1)Reebok Ahary Runner    1,080 B\n2)Reebok FSTR Flexweave  1,470 B\n3)Reebok Triplehall 7.0  957 B\n')
        if ads=='1':
            ra = ('Reebok Ahary Runner         3,600 B        70%      1,080 B')
            pra = 3600-(3600*0.7)
            print(input('Reebok Ahary Runner        3,600 B     ลด 70%'))
            a.append(ra)
            p.append(pra)
        elif ads=='2':
            rf = ('Reebok FSTR Flexweave       4,900 B        70%      1,470 B')
            prf = 4900-(4900*0.7)
            print(input('Reebok FSTR Flexweave      4,900 B     ลด 70%'))
            a.append(rf)
            p.append(prf)
        elif ads=='3':
            rt = ('Reebok Triplehall 7.0       3,190 B        70%      957 B')
            prt = 3190-(3190*0.7)
            print(input('Reebok Triplehall 7.0      3,190 B     ลด 70%'))
            a.append(rt)
            p.append(prt)
        else:
            c = input('กรุณากด Enter เพื่อเริ่มรายการใหม่')
    if s=='v':
        v = input('*************Vans*************\n1)Vans Gum old skool    1,800 B\n2)Vans old skool  1,800 B\n3)Vans Slip-on  1500 B\n')
        if v=='1':
            vg = ('Vans Gum old skool          1,800 B        10%      1,620 B')
            pvg = 1800-(1800*0.1)
            print(input('Vans Gum old skool        1,800 B     ลด 10%'))
            a.append(vg)
            p.append(pvg)
        elif v=='2':
            vos = ('Vans old skool              1,800 B        10%      1,620 B')
            pvos = 1800-(1800*0.1)
            print(input('Vans old skool      1,800 B     ลด 10%'))
            a.append(vos)
            p.append(pvos)
        elif v=='3':
            vso = ('Vans Slip-on                1,500 B        10%      1,350 B')
            pvso = 1500-(1500*0.1)
            print(input('Vans Slip-on      1,500 B     ลด 10%'))
            a.append(vso)
            p.append(pvso)
        else:
            c = input('กรุณากด Enter เพื่อเริ่มรายการใหม่')
            
    if s== 'x':
        print('ขอบคุณที่มาใช้บริการครับ')
        break
    #print('สินค้าใส่ตระกร้าเรียบร้อย')
    #input('ยอดที่ต้องชำระ')
    if s== 'b':
        print('{0:-<60}'.format("")) 
        print('{0:-<30}{1:-<15}{2:-<10}{3:-<10}'.format('รุ่น','ราคา','ส่วนลด','จ่ายจริง'))
        print('{0:-<60}'.format(""))
        count = 0
        for d in a:
            count += 1
            print(count,end=") ")
            print(d)
        
        print('{0:-<60}'.format(""))
        sum = 0
        for n in p:
            sum += n
        print('รวมเป็นเงิน                                            ', sum,'B')
    
        print('{0:-<60}'.format(""))
        print('\n')
        input('เลือกสินค้าต่อกด/กลับหน้าหลัก Enter')