
#################### IMPORTACION DE LIBRERIAS REQUERIDAS ####################



presupuesto_ventas = ""
presupuesto_compras =  ""



while True:
    print("""\n
    -----------PRESUPUESTO MAESTRO----------
    1) Presupuesto De Ventas
    2) Determinacion del saldo de Clientes y Flujo de entrada
    3) Presupuesto de produccion
    4) Presupuesto de requerimiento de Materiales
    5) Presupuesto De Compras de Materiales
    6) Determinacion del Saldo de proveedores y flujo de salida
    7) Presupuesto de Mano de Obra Directa
    8) Presupuesto de Gatos Indirectos de Fabricacion
    9) Presupuesto De Gastos de Operacion
    10) Determinacion del Costo Unitario de Productos Terminados
    11) Valuacion de Inventarios Finales
    12) Presupuesto Financiero
    13) Estado De Resultados
    14) Estado de flujo de efectivo
    15) Estado De Situacion Financiera
    16)Salir
    -------------------------------------""")
    presupuesto = input("\nIngresa una opcion del menu: ")

    #Salir
    if presupuesto == "16":
        break

    #Presupuesto de ventas
    if presupuesto == "1":
        while True:
            producto = input("Producto a agregar el importe de venta: \n1.Tenis Deportivos \n2.Tenis Vans \n3.Tenis Ligeros \n4.Consultar el importe total: \n")
            if producto =="1":
                        unidades_vendidas_1_s1 = int(input("Ingrese Las Unidades a Vender de los tenis deportivos del semestre 1:  "))
                        precio_venta_1_s1 = float(input("Ingrese el precio de venta de los tenis deportivos del semestre 1: "))
                        unidades_vendidas_1_s2 = int(input("Ingrese Las Unidades a Vender de los tenis deportivos del semestre 2:  "))
                        precio_venta_1_s2 = float(input("Ingrese el precio de venta de los tenis deportivos del semestre 2: "))

                        importe_venta_1_s1 = (precio_venta_1_s1 * unidades_vendidas_1_s1)
                        importe_venta_1_s2 = (precio_venta_1_s2 * unidades_vendidas_1_s2)
                        imp_p1_total = (importe_venta_1_s1 + importe_venta_1_s2)
                        print()
                        print(f"El importe de venta anual para los tenis deportivos es de: ${imp_p1_total:,}")
                        print()
                        continue

            if producto =="2":
                        unidades_vendidas_2_s1 = int(input("Ingrese Las Unidades a Vender de los tenis vans del semestre 1:  "))
                        precio_venta_2_s1 = float(input("Ingrese el precio de venta de los tenis vans del semestre 1: "))
                        unidades_vendidas_2_s2 = int(input("Ingrese Las Unidades a Vender de los tenis vans del semestre 2:  "))
                        precio_venta_2_s2 = float(input("Ingrese el precio de venta de los tenis vans del semestre 2: "))

                        importe_venta_2_s1 = (precio_venta_2_s1 * unidades_vendidas_2_s1)
                        importe_venta_2_s2 = (precio_venta_2_s2 * unidades_vendidas_2_s2)
                        imp_p2_total = (importe_venta_2_s1 + importe_venta_2_s2)
                        print()
                        print(f"El importe de venta anual para los tenis vans es de: ${imp_p2_total:,}")
                        print()
                        continue

            if producto =="3":
                        unidades_vendidas_3_s1 = int(input("Ingrese Las Unidades a Vender de tenis ligeros del semestre 1:  "))
                        precio_venta_3_s1 = float(input("Ingrese el precio de venta de tenis ligeros del semestre 1: "))
                        unidades_vendidas_3_s2 = int(input("Ingrese Las Unidades a Vender de tenis ligeros del semestre 2:  "))
                        precio_venta_3_s2 = float(input("Ingrese el precio de venta de tenis ligeros del semestre 2: "))

                        importe_venta_3_s1 = (precio_venta_3_s1 * unidades_vendidas_3_s1)
                        importe_venta_3_s2 = (precio_venta_3_s2 * unidades_vendidas_3_s2)
                        imp_p3_total = (importe_venta_3_s1 + importe_venta_3_s2)
                        print()
                        print(f"El importe de venta anual para los tenis ligeros es de: ${imp_p3_total:,}")
                        print()
                        continue
            
            if producto =="4":
                        total_de_ventasx1semestre = (importe_venta_1_s1 + importe_venta_2_s1 + importe_venta_3_s1)
                        total_de_ventasx2semestre = (importe_venta_1_s2 + importe_venta_2_s2 + importe_venta_3_s2)
                        print()
                        print(f'Total de ventas del Primer Semestre: ${total_de_ventasx1semestre:,}')
                        print()
                        print(f'Total de ventas del Segundo Semestre: ${total_de_ventasx2semestre:,}')
                        print()
                        total_venta_anual =(imp_p1_total + imp_p2_total + imp_p3_total)
                        print()
                        print(f'Total de Ventas Anual ${total_venta_anual:,}')
                        print()
                        break

    #Determinacion del saldo de Clientes y Flujo de entrada
    if presupuesto == "2":
      total_de_clientes = ""
      total_de_entradas = ""
      while True:

          saldo_cliente = float(input("Ingrese el saldo de clientes 31-Dic-2020: "))
          total_de_clientes = (saldo_cliente + total_venta_anual)

          print('Entradas de efectivo')
          cobranza_21= float(input("Cantidad a cobrar en el año 2021: "))
          total_de_entradas =(cobranza_21 + saldo_cliente)
          print(f'El total de clientes 2021: {total_de_clientes:,}')
          print(f'Total de entradas del 2021: ${total_de_entradas:,}')

          saldo_clientes = (total_de_clientes - total_de_entradas)
          print(f'El saldo de clientes del 2021: ${saldo_clientes:,}')
          break

    #Presupuesto de produccion
    if presupuesto == "3":
        while True:
          print("1.Tenis deportivos  \n2.Vans  \n3.Tenis ligeros \n4.Terminar")
          opcion = input("Producto a Escoger: ")

          if opcion == "1":
            inv_final_p1_s1 = int(input("Cual es el inventario final de los tenis deportivos del Semestre 1: "))
            inv_final_p1_s2 = int(input("Cual es el inventario final de los tenis deportivos del Semestre 2: "))
            tot_u_p1_s1 = (inv_final_p1_s1 + unidades_vendidas_1_s1)
            tot_u_p1_s2 = (inv_final_p1_s2 + unidades_vendidas_1_s2)

            inv_inicial_p1_s1 = int(input("Cual es el inventario inicial de los tenis deportivos del Semestre 1: "))
            inv_inicial_p1_s2 = int(input("Cual es el inventario inicial de los tenis deportivos del Semestre 2: "))
            u_producir_p1_s1 = (tot_u_p1_s1 - inv_inicial_p1_s1)
            print()
            print(f"Las unidades a producir de los tenis deportivos en el semestre 1 es: {u_producir_p1_s1:,}")
            print()
            u_producir_p1_s2 = (tot_u_p1_s2 - inv_inicial_p1_s2)
            print(f"Las unidades a producir de los tenis deportivos en el semestre 2 es: {u_producir_p1_s2:,}")
            continue

          if opcion == "2":
            inv_final_p2_s1 = int(input("Cual es el inventario final de los vans del Semestre 1: "))
            inv_final_p2_s2 = int(input("Cual es el inventario final de los vans del Semestre 2: "))
            tot_u_p2_s1 = (inv_final_p2_s1 + unidades_vendidas_2_s1)
            tot_u_p2_s2 = (inv_final_p2_s2 + unidades_vendidas_2_s2)

            inv_inicial_p2_s1 = int(input("Cual es el inventario inicial de los vans del Semestre 1: "))
            inv_inicial_p2_s2 = int(input("Cual es el inventario inicial de los vans del Semestre 2: "))
            u_producir_p2_s1 = (tot_u_p2_s1 - inv_inicial_p2_s1)
            print()
            print(f"Las unidades a producir de los vans en el semestre 1 es: {u_producir_p2_s1:,}")
            print()
            u_producir_p2_s2 = (tot_u_p2_s2 - inv_inicial_p2_s2)
            print(f"Las unidades a producir de los vans en el semestre 2 es: {u_producir_p2_s2:,}")
            print()
            continue

          if opcion == "3":
            inv_final_p3_s1 = int(input("Cual es el inventario final de los tenis ligeros del Semestre 1: "))
            inv_final_p3_s2 = int(input("Cual es el inventario final de los tenis ligeros del Semestre 2: "))
            tot_u_p3_s1 = (inv_final_p3_s1 + unidades_vendidas_3_s1)
            tot_u_p3_s2 = (inv_final_p3_s2 + unidades_vendidas_3_s2)

            inv_inicial_p3_s1 = int(input("Cual es el inventario inicial de los tenis ligeros del Semestre 1: "))
            inv_inicial_p3_s2 = int(input("Cual es el inventario inicial de los tenis ligeros del Semestre 2: "))
            u_producir_p3_s1 = (tot_u_p3_s1 - inv_inicial_p3_s1)
            print()
            print(f"Las unidades a producir de los tenis ligeros en el semestre 1 es: {u_producir_p3_s1:,}")
            print()
            u_producir_p3_s2 = (tot_u_p3_s2 - inv_inicial_p3_s2)
            print(f"Las unidades a producir de los tenis ligeros en el semestre 2 es: {u_producir_p3_s2:,}")
            print()
            
            continue
          
          if opcion == "4":
            p1_tot_up = (u_producir_p1_s1 + u_producir_p1_s2 )
            print(f'Total de unidades a producir al año de los tenis deportivos: {p1_tot_up:,} ')
            p2_tot_up = (u_producir_p2_s1 + u_producir_p2_s2)
            print(f'Total de unidades a producir al año de los vans: {p2_tot_up:,} ')
            p3_tot_up = (u_producir_p3_s1 + u_producir_p3_s2  )
            print(f'Total de unidades a producir al año de los tenis ligeros: {p3_tot_up:,} ')
            break

    #Presupuesto de requerimiento de Materiales
    if presupuesto == "4":
       
        while True:
          print("1.Tenis deportivos  \n2.Vans \n3.Tenis ligeros \n4.Terminar")
          op_producto= input("Elige el producto a agregar: ")
          if op_producto== "1":
             p1_cant_s1= u_producir_p1_s1#cant unidades producir es del 3 
             p1_cant_s2= u_producir_p1_s2
             #Requerimientos de material del producto 1
             p1_matA = float(input("Ingrese el requerimiento del material A: "))
             p1_tot_matAs1 = (p1_matA * p1_cant_s1)
             p1_tot_matAs2 = (p1_matA * p1_cant_s2)
             p1_totalmaterialA =(p1_tot_matAs1 + p1_tot_matAs2)

             p1_matB = float(input("Ingrese el requerimiento del material B: "))
             p1_tot_matBs1 = (p1_matB * p1_cant_s1)
             p1_tot_matBs2 = (p1_matB * p1_cant_s2)
             p1_totalmaterialB =(p1_tot_matBs1 + p1_tot_matBs2)

             p1_matC = float(input("Ingrese el requerimiento del material C: "))
             p1_tot_matCs1 = (p1_matC * p1_cant_s1)
             p1_tot_matCs2 = (p1_matC * p1_cant_s2)
             p1_totalmaterialC =(p1_tot_matCs1 + p1_tot_matCs2)

             #Totales de material del primer producto sobre SEMESTRES
             print()
             print(f'Total del material A requerido de tenis deportivos al Primer Semestre : {p1_tot_matAs1:,}')
             print(f'Total del material A requerido de tenis deportivos al Segundo Semestre: {p1_tot_matAs2:,}')
             print()

             print(f'Total del material B requerido de tenis deportivos al Primer Semestre : {p1_tot_matBs1:,}')
             print(f'Total del material B requerido de tenis deportivos al Segundo Semestre: {p1_tot_matBs2:,}')
             print()

             print(f'Total del material C requerido de tenis deportivos al Primer Semestre : {p1_tot_matCs1:,}')
             print(f'Total del material C requerido de tenis deportivos al Segundo Semestre: {p1_tot_matCs2:,}')
             print()

             #Totales de material del primer producto al AÑO
             print(f'Total del material A requerido del primer producto al año : {p1_totalmaterialA:,}')
             print(f'Total del material B requerido del primer producto al año: {p1_totalmaterialB:,}')
             print(f'Total del material C requerido del primer producto al año: {p1_totalmaterialC:,}')
             continue

          if op_producto=="2":
             p2_cant_s1=u_producir_p2_s1
             p2_cant_s2=u_producir_p2_s2
             #Requerimientos de material del producto 2
             p2_matA = float(input("Ingrese el requerimiento del material A: "))
             p2_tot_matAs1 = (p2_matA * p2_cant_s1)
             p2_tot_matAs2 = (p2_matA * p2_cant_s2)
             p2_totalmaterialA =(p2_tot_matAs1 + p2_tot_matAs2)

             p2_matB = float(input("Ingrese el requerimiento del material B: "))
             p2_tot_matBs1 = (p2_matB * p2_cant_s1)
             p2_tot_matBs2 = (p2_matB * p2_cant_s2)
             p2_totalmaterialB =(p2_tot_matBs1 + p2_tot_matBs2)

             p2_matC = float(input("Ingrese el requerimiento del material C: "))
             p2_tot_matCs1 = (p2_matC * p2_cant_s1)
             p2_tot_matCs2 = (p2_matC * p2_cant_s2)
             p2_totalmaterialC = (p2_tot_matCs1 + p2_tot_matCs2)

             #Totales de material del segundo producto sobre SEMESTRES
             print()
             print(f'Total del material A requerido de los vans al Primer Semestre : {p2_tot_matAs1:,}')
             print(f'Total del material A requerido de los vans al Segundo Semestre: {p2_tot_matAs2:,}')
             print()

             print(f'Total del material B requerido de los vans al Primer Semestre : {p2_tot_matBs1:,}')
             print(f'Total del material B requerido de los vans al Segundo Semestre: {p2_tot_matBs2:,}')
             print()

             print(f'Total del material C requerido de los vans al Primer Semestre : {p2_tot_matCs1:,}')
             print(f'Total del material C requerido de los vans al Segundo Semestre: {p2_tot_matCs2:,}')
             print()

             #Totales de material del segundo producto al AÑO
             print(f'Total del material A requerido de los vans al año : {p2_totalmaterialA:,}')
             print(f'Total del material B requerido de los vans al año: {p2_totalmaterialB:,}')
             print(f'Total del material C requerido de los vans al año: {p2_totalmaterialC:,}')
             continue
            
          if op_producto=="3":
             p3_cant_s1=u_producir_p3_s1
             p3_cant_s2=u_producir_p3_s2
             #Requerimientos de material del producto 3
             p3_matA = float(input("Ingrese el requerimiento del material A: "))
             p3_tot_matAs1 = (p3_matA * p3_cant_s1)
             p3_tot_matAs2 = (p3_matA * p3_cant_s2)
             p3_totalmaterialA =(p3_tot_matAs1 + p3_tot_matAs2)
             
             p3_matB = float(input("Ingrese el requerimiento del material B: "))
             p3_tot_matBs1 = (p3_matB * p3_cant_s1)
             p3_tot_matBs2 = (p3_matB * p3_cant_s2)
             p3_totalmaterialB =(p3_tot_matBs1 + p3_tot_matBs2)

             p3_matC = float(input("Ingrese el requerimiento del material C: "))
             p3_tot_matCs1 = (p3_matC * p3_cant_s1)
             p3_tot_matCs2 = (p3_matC * p3_cant_s2)
             p3_totalmaterialC =(p3_tot_matCs1 + p3_tot_matCs2)

             #Totales de material del tercer producto sobre SEMESTRES
             print()
             print(f'Total del material A requerido de tenis ligeros al Primer Semestre : {p3_tot_matAs1:,}')
             print(f'Total del material A requerido de tenis ligeros al Segundo Semestre: {p3_tot_matAs2:,}')
             print()

             print(f'Total del material B requerido de tenis ligeros al Primer Semestre : {p3_tot_matBs1:,}')
             print(f'Total del material B requerido de tenis ligeros al Segundo Semestre: {p3_tot_matBs2:,}')
             print()

             print(f'Total del material C requerido de tenis ligeros al Primer Semestre : {p3_tot_matCs1:,}')
             print(f'Total del material C requerido de tenis ligeros al Segundo Semestre: {p3_tot_matCs2:,}')

             #Totales de material del tercer producto al año
             print()
             print(f'Total del material A requerido de tenis ligeros al año : {p3_totalmaterialA:,}')
             print(f'Total del material B requerido de tenis ligeros al año: {p3_totalmaterialB:,}')
             print(f'Total del material C requerido de tenis ligeros al año: {p3_totalmaterialC:,}')
             print()

             print("Total de requerimientos(gramos)")
             #SUMA DEL TOTAL DEL MATERIAL A DE TODOS LOS PRODUCTOS
             requerimiento_semestre1_matA = (p1_tot_matAs1 + p2_tot_matAs1 + p3_tot_matAs1)
             requerimiento_semestre2_matA = (p1_tot_matAs2 + p2_tot_matAs2 + p3_tot_matAs2)
             #SUMA DEL TOTAL DEL MATERIAL B DE TODOS LOS PRODUCTOS
             requerimiento_semestre1_matB = (p1_tot_matBs1 + p2_tot_matBs1 + p3_tot_matBs1)
             requerimiento_semestre2_matB = (p1_tot_matBs2 + p2_tot_matBs2 + p3_tot_matBs2)
             #SUMA DEL TOTAL DEL MATERIAL B DE TODOS LOS PRODUCTOS
             requerimiento_semestre1_matC = (p1_tot_matCs1 + p2_tot_matCs1 + p3_tot_matCs1)
             requerimiento_semestre2_matC = (p1_tot_matCs2 + p2_tot_matCs2 + p3_tot_matCs2)
             
             print()
             print("                  Primer Semestre        Segundo Semestre ")
             print(f'Material A:       {requerimiento_semestre1_matA:,}               {requerimiento_semestre2_matA:,}')
             print(f'Material B:       {requerimiento_semestre1_matB:,}               {requerimiento_semestre2_matB:,}')
             print(f'Material C:       {requerimiento_semestre1_matC:,}               {requerimiento_semestre2_matC:,}')
             continue
        
          if op_producto == "4":
             break

    #Presupuesto De Compras de Materiales
    if presupuesto == "5":
        while True:
          print("1.Material A  \n2.Material B  \n3.Material C \n4.Terminar")
          op_producto= input("Elige el material de los datos a agregar: ")
          if op_producto== "1":
            #DATOS A PREGUNTAR SOBRE EL MATERIAL A DEL SEMESTRE 1
            inventario_final_producto1_semestre1 = int(input("Cual fue el inventario final para el MATERIAL A en el primer semestre: "))
            inventario_inicial_producto1_semestre1 = int(input("Cual fue el inventario inicial para el MATERIAL A en el primer semestre: "))
            precio_compra_producto1_semestre1 = float(input("Cual fue el precio de compra para el MATERIAL A en el primer semestre: "))
            material_comparar_producto1_semestre1 = (requerimiento_semestre1_matA + inventario_final_producto1_semestre1 - inventario_inicial_producto1_semestre1 )
            total_producto1_dinero_semestre1 = (material_comparar_producto1_semestre1 * precio_compra_producto1_semestre1)
            dinero_producto1_semestre1 = (total_producto1_dinero_semestre1)

            print()
            print(f"El total de material A comprar en el primer semestre en pesos es de ${dinero_producto1_semestre1:,}")
            print()

            #DATOS A PREGUNTAR SOBRE EL MATERIAL A DEL SEMESTRE 2
            inventario_final_producto1_semestre2 = int(input("Cual fue el inventario final para el MATERIAL A en el segundo semestre: "))
            inventario_inicial_producto1_semestre2 = int(input("Cual fue el inventario inicial para el MATERIAL A en el segundo semestre: "))
            precio_compra_producto1_semestre2 = float(input("Cual fue el precio de compra para el MATERIAL A en el segundo semestre: "))
            material_comparar_producto1_semestre2 = (requerimiento_semestre2_matA + inventario_final_producto1_semestre2 - inventario_inicial_producto1_semestre2 )
            total_producto1_dinero_semestre2 = (material_comparar_producto1_semestre2 * precio_compra_producto1_semestre2)
            dinero_producto1_semestre2 = (total_producto1_dinero_semestre2)
            
            print()
            print(f"El total de MATERIAL A a comprar en el segundo semestre en pesos es de: ${dinero_producto1_semestre2:,}")
            print()

            dinero_producto1_final = (dinero_producto1_semestre1 + dinero_producto1_semestre2)

            print()
            print("**********************************************************************")
            print(f"El total de MATERIAL A anual a comprar en pesos fue de: ${dinero_producto1_final:,}  ")
            print("**********************************************************************")
            print()
            continue

          if op_producto=="2":
            #DATOS A PREGUNTAR SOBRE EL MATERIAL A DEL SEMESTRE 1
            inventario_final_producto2_semestre1 = int(input("Cual fue el inventario final para el MATERIAL B en el primer semestre: "))
            inventario_inicial_producto2_semestre1 = int(input("Cual fue el inventario inicial para el MATERIAL B en el primer semestre: "))
            precio_compra_producto2_semestre1 = float(input("Cual fue el precio de compra para el MATERIAL B en el primer semestre: "))
            material_comparar_producto2_semestre1 = (requerimiento_semestre1_matB + inventario_final_producto2_semestre1 - inventario_inicial_producto2_semestre1 )
            total_producto2_dinero_semestre1 = (material_comparar_producto2_semestre1 * precio_compra_producto2_semestre1)
            dinero_producto2_semestre1 = (total_producto2_dinero_semestre1)

            print()
            print(f"El total de material B comprar en el primer semestre en pesos es de ${dinero_producto2_semestre1:,}")
            print()

            #DATOS A PREGUNTAR SOBRE EL MATERIAL A DEL SEMESTRE 2
            inventario_final_producto2_semestre2 = int(input("Cual fue el inventario final para el MATERIAL B en el segundo semestre: "))
            inventario_inicial_producto2_semestre2 = int(input("Cual fue el inventario inicial para el MATERIAL B en el segundo semestre: "))
            precio_compra_producto2_semestre2 = float(input("Cual fue el precio de compra para el MATERIAL B en el segundo semestre: "))
            material_comparar_producto2_semestre2 = (requerimiento_semestre2_matB + inventario_final_producto2_semestre2 - inventario_inicial_producto2_semestre2 )
            total_producto1_dinero_semestre2 = (material_comparar_producto2_semestre2 * precio_compra_producto2_semestre2)
            dinero_producto2_semestre2 = (total_producto1_dinero_semestre2)
            
            print()
            print(f"El total de MATERIAL B a comprar en el segundo semestre en pesos es de: ${dinero_producto2_semestre2:,}")
            print()

            dinero_producto2_final = (dinero_producto2_semestre1 + dinero_producto2_semestre2)

            print()
            print("**********************************************************************")
            print(f"El total de MATERIAL B anual a comprar en pesos fue de: ${dinero_producto2_final:,}  ")
            print("**********************************************************************")
            print()
            continue
            
          if op_producto=="3":
            #DATOS A PREGUNTAR SOBRE EL MATERIAL A DEL SEMESTRE 1
            inventario_final_producto3_semestre1 = int(input("Cual fue el inventario final para el MATERIAL C en el primer semestre: "))
            inventario_inicial_producto3_semestre1 = int(input("Cual fue el inventario inicial para el MATERIAL C en el primer semestre: "))
            precio_compra_producto3_semestre1 = float(input("Cual fue el precio de compra para el MATERIAL C en el primer semestre: "))
            material_comparar_producto3_semestre1 = (requerimiento_semestre1_matC + inventario_final_producto3_semestre1 - inventario_inicial_producto3_semestre1 )
            total_producto3_dinero_semestre1 = (material_comparar_producto3_semestre1 * precio_compra_producto3_semestre1)
            dinero_producto3_semestre1 = (total_producto3_dinero_semestre1)

            print()
            print(f"El total de material C comprar en el primer semestre en pesos es de ${dinero_producto3_semestre1:,}")
            print()

            #DATOS A PREGUNTAR SOBRE EL MATERIAL A DEL SEMESTRE 2
            inventario_final_producto3_semestre2 = int(input("Cual fue el inventario final para el MATERIAL C en el segundo semestre: "))
            inventario_inicial_producto3_semestre2 = int(input("Cual fue el inventario inicial para el MATERIAL C en el segundo semestre: "))
            precio_compra_producto3_semestre2 = float(input("Cual fue el precio de compra para el MATERIAL C en el segundo semestre: "))
            material_comparar_producto3_semestre2 = (requerimiento_semestre2_matC + inventario_final_producto3_semestre2 - inventario_inicial_producto3_semestre2 )
            total_producto3_dinero_semestre2 = (material_comparar_producto3_semestre2 * precio_compra_producto3_semestre2)
            dinero_producto3_semestre2 = (total_producto3_dinero_semestre2)
            
            print()
            print(f"El total de MATERIAL C a comprar en el segundo semestre en pesos es de: ${dinero_producto3_semestre2:,}")
            print()

            dinero_producto3_final = (dinero_producto3_semestre1 + dinero_producto3_semestre2)

            print()
            print("**********************************************************************")
            print(f"El total de MATERIAL C anual a comprar en pesos fue de: ${dinero_producto3_final:,}  ")
            print("**********************************************************************")
            print()
            continue
        
          if op_producto == "4":
            #COMPRAS TOTALES DEL SEMESTRE 1
            suma_compra_semestre1 = (dinero_producto3_semestre1 + dinero_producto2_semestre1 + dinero_producto1_semestre1)

            print()
            print(f"Compras totales del semestre 1: ${suma_compra_semestre1:,}")
            print()

            #COMPRAS TOTALES DEL SEMESTRE 2
            suma_compra_semestre2 = (dinero_producto3_semestre2 + dinero_producto2_semestre2 + dinero_producto1_semestre2)
            print()
            print(f"Compras totales del semestre 2: ${suma_compra_semestre2:,}")
            print()

            #COMPRAS TOTALES ANUAL
            suma_compra_final_anual = (suma_compra_semestre1 + suma_compra_semestre2)

            print()
            print(f"Compras totales en el año: ${suma_compra_final_anual:,}")
            print()

            break

    #Determinacion del Saldo de proveedores y flujo de salida
    if presupuesto == "6":
      while True:
          saldo_de_proveedores = float(input("Ingrese el saldo de proveedores 31-Dic-2020: "))
          compras = suma_compra_final_anual#Del 5
          total_de_proveedores2021 = (saldo_de_proveedores + compras)
          print(f'El total de proveedores del 2021 es de: {total_de_proveedores2021:,}')

          print("Salidas de efectivo")
          proveedores_2021 = (compras / 2)
          total_salidas2021=(saldo_de_proveedores + proveedores_2021)
          print(f'El total de salidas del 2021 es: ${total_salidas2021:,}')
          saldo_proveedores = total_de_proveedores2021 - total_salidas2021
          print(f'Saldo de proveedores del 2021: ${saldo_proveedores:,}')
          break

    #Presupuesto de Mano de Obra Directa
    if presupuesto == "7":
      hora_requerida_pantalon = float(input("Cuantas horas se requieren por unidad de los tenis deportivos: "))
      hora_requerida_short = float(input("Cuantas horas se requieren por unidad de los vans: "))
      hora_requerida_cargo = float(input("Cuantas horas se requieren por unidad de los tenis ligeros: "))
      cuota_hora_semestre1 = float(input("Ingrese el precio de cuota por unidad del semestre 1: "))
      cuota_hora_semestre2 = float(input("Ingrese el precio de cuota por unidad del semestre 2: "))
      while True:
        print("1.Tenis deportivos   \n2.Vans   \n3.Tenis ligeros \n4.Terminar")
        producto = input("Elige el producto a agregar: ") 
        
        if producto == "1":
            total_horas_requeridas_pantalon_semestre1 = (u_producir_p1_s1 * hora_requerida_pantalon)
            print()
            print(f"Las horas requeridas para la produccion de los tenis deportivos del primer semestre son de: {total_horas_requeridas_pantalon_semestre1:,}")
            print()
            importe_mod_pantalon_sem1 = (total_horas_requeridas_pantalon_semestre1 * cuota_hora_semestre1)
            print()
            print(f"El importe M.O.D para el semestre 1 de los tenis deportivos es de: ${importe_mod_pantalon_sem1:,}")
            print()
            total_horas_requeridas_pantalon_semestre2 = (u_producir_p1_s2 * hora_requerida_pantalon)
            print()
            print(f"Las horas requeridas para la produccion de los tenis deportivos del segundo semestre son de: {total_horas_requeridas_pantalon_semestre2:,}")
            print()
            importe_mod_pantalon_sem2 = (total_horas_requeridas_pantalon_semestre2 * cuota_hora_semestre2)
            print()
            print(f"El importe M.O.D para el semestre 2 de los tenis deportivos es de: ${importe_mod_pantalon_sem2:,}")
            print()
            importe_mod_anual_pantalon = (importe_mod_pantalon_sem1 + importe_mod_pantalon_sem2)
            print()
            print(f"El importe M.O.D para los tenis deportivos al año es de: ${importe_mod_anual_pantalon:,}")
            print()
        if producto == "2":
            total_horas_requeridas_short_semestre1 = (u_producir_p2_s1 * hora_requerida_short)
            print()
            print(f"Las horas requeridas para la produccion de los vans del primer semestre son de: {total_horas_requeridas_short_semestre1:,}")
            print()
            importe_mod_short_sem1 = (total_horas_requeridas_short_semestre1 * cuota_hora_semestre1)
            print()
            print(f"El importe M.O.D para el semestre 1 de los vans es de: ${importe_mod_short_sem1:,}")
            print()
            total_horas_requeridas_short_semestre2 = (u_producir_p2_s2 * hora_requerida_short)
            print()
            print(f"Las horas requeridas para la produccion de los vans es del segundo semestre son de: {total_horas_requeridas_short_semestre2:,}")
            print()
            importe_mod_short_sem2 = (total_horas_requeridas_short_semestre2 * cuota_hora_semestre2)
            print()
            print(f"El importe M.O.D para el semestre 2 de los vans es de: ${importe_mod_short_sem2:,}")
            print()
            importe_mod_anual_short = (importe_mod_short_sem1 + importe_mod_short_sem2)
            print()
            print(f"El importe M.O.D para los vans al año es de: ${importe_mod_anual_short:,}")
            print()
        if producto == "3":
            total_horas_requeridas_cargo_semestre1 = (u_producir_p3_s1 * hora_requerida_cargo)
            print()
            print(f"Las horas requeridas para la produccion los tenis ligeros del primer semestre son de: {total_horas_requeridas_cargo_semestre1:,}")
            print()
            importe_mod_cargo_sem1 = (total_horas_requeridas_cargo_semestre1 * cuota_hora_semestre1)
            print()
            print(f"El importe M.O.D para el semestre 1 de los tenis ligeros es de: ${importe_mod_cargo_sem1:,}")
            print()
            total_horas_requeridas_cargo_semestre2 = (u_producir_p3_s2 * hora_requerida_cargo)
            print()
            print(f"Las horas requeridas para la produccion de los tenis ligeros del segundo semestre son de: {total_horas_requeridas_cargo_semestre2:,}")
            print()
            importe_mod_cargo_sem2 = (total_horas_requeridas_cargo_semestre2 * cuota_hora_semestre2)
            print()
            print(f"El importe M.O.D para el semestre 2 de los tenis ligeros es de: ${importe_mod_cargo_sem2:,}")
            print()
            importe_mod_anual_cargo = (importe_mod_cargo_sem1 + importe_mod_cargo_sem2)
            print()
            print(f"El importe M.O.D para los tenis ligeros al año es de: ${importe_mod_anual_cargo:,}")
            print()
        if producto == "4":
            total_horas_requeridas_anuales = (total_horas_requeridas_pantalon_semestre1 + total_horas_requeridas_pantalon_semestre2 + total_horas_requeridas_cargo_semestre1 + total_horas_requeridas_cargo_semestre2 + total_horas_requeridas_short_semestre1 + total_horas_requeridas_short_semestre2)
            importe_mod_anual_productos = (importe_mod_anual_cargo + importe_mod_anual_pantalon + importe_mod_anual_short)
            print()
            print(f"El importe M.O.D total de los tenis es de: ${importe_mod_anual_productos:,}")
            print()
            print(f"El total de horas requeridas fueron de: {total_horas_requeridas_anuales:,}")
            break

    #Presupuesto de Gatos Indirectos de Fabricacion
    if presupuesto == "8":
        depre = float(input("Ingrese el monto de depreciacion anual: "))
        segur = float(input("Ingrese el monto de seguros anual: "))
        vari = float(input("Ingrese el monto de varios anual: "))
        while True:
            print()
            opcion = input("Ingrese los datos de \n1.Primer semestre \n2.Segundo semestre \n3.Terminado\n")
            if opcion == "1":
            #PRIMER SEMESTRE
                mantenimiento_sem1 = float(input("Ingrese el monto de mantenimiento para el primer semestre: "))
                energeticos_sem1 = float(input("Ingrese el monto de energeticos primer semestre: "))
                depreciacion = (depre / 2)
                seguros = (segur / 2)
                varios = (vari / 2)
                total_de_gif1 = (depreciacion + seguros + mantenimiento_sem1 + energeticos_sem1 + varios)
                print()
                print(f'El total de G.I.F. del primer semestre es de: ${total_de_gif1:,}')
                print()
                continue

            if opcion == "2":
            #SEGUNDO SEMESTRE
                mantenimiento2 = float(input("Ingrese el monto de mantenimiento para el segundo semestre: "))
                energeticos2 = float(input("Ingrese el monto de energeticos para el segundo semestre: "))
                depreciacion2 = (depre / 2)
                seguros2 = (segur / 2)
                varios2 = (vari / 2)
                total_de_gif2 = (depreciacion2 + seguros2 + mantenimiento2 + energeticos2 + varios2)
                print()
                print(f'El total de G.I.F. del segundo semestre es de: ${total_de_gif2:,}')
                print()
                continue

            if opcion == "3":
            #ANUAL
                total_gif = (total_de_gif1 + total_de_gif2)
                print()
                print(f'Total de Gastos Indirectos de fabricacion al año ${total_gif:,}')
                print()
                costo_hora_gif = (total_gif/total_horas_requeridas_anuales)
                print(f"El costo por hora del Gasto indirecto de fabricaion es de: ${costo_hora_gif:,}")
                break

    #Presupuesto De Gastos de Operacion
    if presupuesto == "9":
        depreciacion_9 = float(input("Cual es la depreceacion anual: "))
        sueldos_salarios_9 = float(input("Cual es el sueldo y salarios anuales: "))
        interereses_9 = float(input("Cual es el total de los intereses anuales del prestamo: "))
        print()
        while True:
            semestre = input("Ingrese los datos de \n1.Primer semestre \n2.Segundo semestre \n3.Terminado \n")
            
            if semestre == "1":
                varios_sem1 = float(input("Cuales fueron los gastos varios para el primer semestre: "))
                depre_sem1 = (depreciacion_9/2)
                print()
                print(f"La depreciacion para el primer semestre es de: ${depre_sem1:,}")
                print()
                sueldos_sem1 = (sueldos_salarios_9/2)
                print()
                print(f"Los sueldos y salarios para el semestre 1 es de: ${sueldos_sem1:,}")
                print()
                comisiones_sem1 = (total_de_ventasx1semestre * .01)
                print()
                print(f"La comision para el semestre 1 es de: ${comisiones_sem1:,}")
                print()
                intereses_prestamo_sem1 = (interereses_9/2)
                print()
                print(f"Los intereses para el semestre 1 es de: ${intereses_prestamo_sem1:,}")
                print()
                total_gastos_operacion_sem1 = (varios_sem1 + depre_sem1 + sueldos_sem1 + comisiones_sem1 + intereses_prestamo_sem1)
                print()
                print(f"El total de gastos de operacion para el primer semestre es de: ${total_gastos_operacion_sem1:,}")
                print()
                continue
            if semestre == "2":
                varios_sem2 = float(input("Cuales fueron los gastos varios para el segundo semestre: "))
                depre_sem2 = (depreciacion_9/2)
                print()
                print(f"La depreciacion para el segundo semestre es de: ${depre_sem2:,}")
                print()
                sueldos_sem2 = (sueldos_salarios_9/2)
                print()
                print(f"Los sueldos y salarios para el semestre 2 es de: ${sueldos_sem2:,}")
                print()
                comisiones_sem2 = (total_de_ventasx2semestre * .01)
                print()
                print(f"La comision para el semestre 2 es de: ${comisiones_sem2:,}")
                print()
                intereses_prestamo_sem2 = (interereses_9/2)
                print()
                print(f"Los intereses para el semestre 2 es de: ${intereses_prestamo_sem2:,}")
                print()
                total_gastos_operacion_sem2 = (varios_sem2 + depre_sem2 + sueldos_sem2 + comisiones_sem2 + intereses_prestamo_sem2)
                print()
                print(f"El total de gastos de operacion para el primer semestre es de: ${total_gastos_operacion_sem2:,}")
                print()
                continue
            if semestre == "3":
                total_gastos_operacion_2021 = (total_gastos_operacion_sem2 + total_gastos_operacion_sem1)
                print()
                print(f"Los gastos totales de operacion del 2021 son de: ${total_gastos_operacion_2021:,}")
                print()
                break

    #Determinacion del Costo Unitario de Productos Terminados
    if presupuesto == "10":
        costo_material_A = precio_compra_producto1_semestre2
        costo_material_B = precio_compra_producto2_semestre2
        costo_material_C = precio_compra_producto3_semestre2
        cuota_mano_obra = cuota_hora_semestre2
        gastoS_indirectos = costo_hora_gif
        while True:
            producto_11 = input("1.Tenis deportivos  \n2.Vans  \n3.Tenis ligeros \n4.Terminar\n")
            
            if producto_11 == "1":
                cant_materiales_a = p1_matA
                cant_materiales_b = p1_matB
                cant_materiales_c = p1_matC
                mano_obra_pantalon = hora_requerida_pantalon
                
                costo_uni_material_A =(cant_materiales_a * costo_material_A)
                costo_uni_material_B =(cant_materiales_b * costo_material_B)
                costo_uni_material_C =(cant_materiales_c * costo_material_C)
                costo_mano_obra = (mano_obra_pantalon * cuota_mano_obra )
                costo_gif = (gastoS_indirectos * mano_obra_pantalon )
                
                costo_uni_total_pantalon = (costo_uni_material_A + costo_uni_material_B + costo_uni_material_C + costo_mano_obra + costo_gif)
                
                print()
                print(f"El costo unitario para los tenis deportivos es de: ${costo_uni_total_pantalon:,}")
                print()
                continue
            
            if producto_11 == "2":
                cant_materiales_short_a = p2_matA
                cant_materiales_short_b = p2_matB
                cant_materiales_short_c = p2_matC
                mano_obra_short = hora_requerida_short
                
                costo_uni_material_short_A =(cant_materiales_short_a * costo_material_A)
                costo_uni_material_short_B =(cant_materiales_short_b * costo_material_B)
                costo_uni_material_short_C =(cant_materiales_short_c * costo_material_C)
                costo_mano_obra_short = (mano_obra_short * cuota_mano_obra )
                costo_gif_short = (gastoS_indirectos * mano_obra_short )
                
                costo_uni_total_short = (costo_uni_material_short_A + costo_uni_material_short_B + costo_uni_material_short_C + costo_mano_obra_short + costo_gif_short)

                print()
                print(f"El costo unitario para los vans es de: ${costo_uni_total_short:,}")
                print()
                continue
            
            if producto_11 == "3":
                cant_materiales_cargo_a = p3_matA
                cant_materiales_cargo_b = p3_matB
                cant_materiales_cargo_c = p3_matC
                mano_obra_cargo = hora_requerida_cargo
                
                costo_uni_material_cargo_A =(cant_materiales_cargo_a * costo_material_A)
                costo_uni_material_cargo_B =(cant_materiales_cargo_b * costo_material_B)
                costo_uni_material_cargo_C =(cant_materiales_cargo_c * costo_material_C)
                costo_mano_obra_cargo = (mano_obra_cargo * cuota_mano_obra )
                costo_gif_cargo = (gastoS_indirectos * mano_obra_cargo )
                
                costo_uni_total_cargo = (costo_uni_material_cargo_A + costo_uni_material_cargo_B + costo_uni_material_cargo_C + costo_mano_obra_cargo + costo_gif_cargo)
                
                print()
                print(f"El costo unitario para los tenis ligeros es de: ${costo_uni_total_cargo:,}")
                print()
                break

    #Valuacion de Inventarios Finales
    if presupuesto == "11":
        
        unidades_a = inventario_final_producto1_semestre2
        unidades_b = inventario_final_producto2_semestre2
        unidades_c = inventario_final_producto3_semestre2
        costo_unitario_a = precio_compra_producto1_semestre2
        costo_unitario_b = precio_compra_producto2_semestre2
        costo_unitario_c = precio_compra_producto3_semestre2
        costo_unitario_pantalon = costo_uni_total_pantalon
        costo_unitario_short = costo_uni_total_short
        costo_unitario_cargo = costo_uni_total_cargo
        unidades_pantalon = inv_final_p1_s2
        unidades_short = inv_final_p2_s2
        unidades_cargo = inv_final_p3_s2
        
        while True:
            material_producto = input("Seleccione si desea saber el inventario Final de \n(1)materiales\n(2)productos\n(3)inventarios finales:  \n")
            
            if material_producto == "1":
                costo_total_a_sem1 = (unidades_a * costo_unitario_a)
                costo_total_b_sem1 = (unidades_b * costo_unitario_b)
                costo_total_c_sem1 = (unidades_c * costo_unitario_c)
                print(f"El costo total para el Material A es : ${costo_total_a_sem1:,}")
                print(f"El costo total para el Material B es : ${costo_total_b_sem1:,}")
                print(f"El costo total para el Material C es : ${costo_total_c_sem1:,}")
                continue
            if material_producto == "2":
                costo_total_a_sem2 = (unidades_pantalon * costo_unitario_pantalon)
                costo_total_b_sem2 = (unidades_short * costo_unitario_short)
                costo_total_c_sem2 = (unidades_cargo * costo_unitario_cargo)
                print(f"El costo total para el Producto Tenis deportivos es : ${costo_total_a_sem2:,}")
                print(f"El costo total para el Producto Vans es : ${costo_total_b_sem2:,}")
                print(f"El costo total para el Producto Tenis ligeros : ${costo_total_c_sem2:,}")
                continue
            if material_producto == "3":
                suma_inventario_final_materiales = (costo_total_a_sem1 + costo_total_b_sem1 + costo_total_c_sem1)
                suma_inventario_final_producto = (costo_total_a_sem2 + costo_total_b_sem2 + costo_total_c_sem2)
                print(f"El inventario final de los materiales es: ${suma_inventario_final_materiales:,}")
                print(f"El inventario final de los productos es de: ${suma_inventario_final_producto:,}")
                break

    #Presupuesto Financiero
    if presupuesto == "12":
        
        saldo_inicial_materiales = float(input("Ingrese el saldo inicial de materiales: "))
        compras_materiales = suma_compra_final_anual
        material_disponible = (saldo_inicial_materiales + compras_materiales)

        print()
        print(f'El material disponible es de {material_disponible:,}')
        print()

        inventario_final_materiales = suma_inventario_final_materiales

        materiales_utilizados = (material_disponible - inventario_final_materiales)

        print()
        print(f'El monto de materiales utilizados es de ${materiales_utilizados:,}')
        print()

        mano_obra_directa = importe_mod_anual_productos
        gastos_fabricacion = total_gif
        costo_de_produccion = (materiales_utilizados + mano_obra_directa + gastos_fabricacion)

        print()
        print(f'El costo de produccion es de ${costo_de_produccion:,}')
        print()

        inventario_ini_prod_terminados = float(input("Ingrese el monto del inventario inicial de productos terminados: "))

        total_produccion_disponible = (costo_de_produccion + inventario_ini_prod_terminados)

        print()
        print(f'El total de produccion disponible es de ${total_produccion_disponible:,}')
        print()

        inventario_fin_prod_terminados = suma_inventario_final_producto
        costo_ventas = (total_produccion_disponible - inventario_fin_prod_terminados)

        print()
        print(f'El costo de ventas es de ${costo_ventas:,}')
        print()

    #Estado De Resultados
    if presupuesto == "13":
        
        ventas_resultados = total_venta_anual
        costos_resultados = costo_ventas
        
        utilidad_bruta_resultados = (ventas_resultados - costos_resultados)
        print()
        print(f"La utilidad bruta es de: ${utilidad_bruta_resultados:,}")
        print()
        
        gastos_resultados = total_gastos_operacion_2021
        
        utilidad_operacion_resultados = (utilidad_bruta_resultados - gastos_resultados)
        
        print()
        print(f"La utilidad de operacion es de: ${utilidad_operacion_resultados:,}")
        print()
        
        impuesto_sobre_renta = (utilidad_operacion_resultados * .3)
        reparto_utilidades_empresa = (utilidad_operacion_resultados * .1)
        
        utilidad_neta = (utilidad_operacion_resultados - impuesto_sobre_renta - reparto_utilidades_empresa)
        
        print()
        print(f"La utilidad neta es de: ${utilidad_neta:,}")
        print()

    #Estado de flujo de efectivo
    if presupuesto == "14":
        while True:
            entradas_salidas_efectivo = input("\n1.Entradas \n2.Salidas \n3.Flujo Efectivo Actual: \n")
            if entradas_salidas_efectivo == "1":
                saldo_inicial_efectivo = float(input("Cual es el saldo incial: "))
                cobranza_flujo_21 = cobranza_21
                cobranza_flujo_20 = saldo_cliente
                
                total_entradas_flujo = (cobranza_flujo_21 + cobranza_flujo_20)
                
                print()
                print(f"El total de entradas es: ${total_entradas_flujo:,}")
                print()
                
                efectivo_disponible_flujo = (total_entradas_flujo + saldo_inicial_efectivo)
                
                print()
                print(f"El efectivo disponible es de: ${efectivo_disponible_flujo:,}")
                print()
                continue
            
            if entradas_salidas_efectivo == "2":
                provedor_21 = proveedores_2021
                provedor_20 = saldo_de_proveedores
                total_gif_salida = total_gif
                gastos_operacion_salida = total_gastos_operacion_2021
                depreciacion_salida = depreciacion_9
                depreciacion_salida_8 = depre
                pago_isr_20 = float(input("Cuanto fue el pago del isr para el 2020: "))
                
                total_mano_obra_directa = importe_mod_anual_productos
                print()
                print(f"El pago de mano obra directa ${total_mano_obra_directa:,}")
                print()
                
                pago_gasto_indirecto_faricacion = (total_gif_salida - depreciacion_salida_8)
                print()
                print(f"El pago de gastos indirectos de fabricacion es de: ${pago_gasto_indirecto_faricacion:,}")
                print()
                
                pago_gastos_operacion = (gastos_operacion_salida - depreciacion_salida )
                print()
                print(f"El pago de gastos de operacion es de: ${pago_gastos_operacion:,}")
                print()
                
                print()
                print(f"El pago de isr para el 2020 fue de: ${pago_isr_20:,}")
                print()
                
                compra_activo_fijo = int(input("Ingresa el activo fijo: "))
                
                total_salidas_14 = (provedor_21 + provedor_20 + total_mano_obra_directa + total_gif_salida + gastos_operacion_salida + compra_activo_fijo + pago_isr_20)
                print()
                print(f"El total de salidas es de: ${total_salidas_14:,}")
                print()
                continue
            
            if entradas_salidas_efectivo == "3":
                flujo_efectivo_actual = (efectivo_disponible_flujo - total_salidas_14)
                print()
                print(f"El flujo de efectivo actual es: ${flujo_efectivo_actual:,}")
                print()
                break

    #Estado De Situacion Financiera
    if presupuesto == "15":
        efectivo_balance = flujo_efectivo_actual
        clientes_balance = total_de_clientes
        
        deudores_balance = float(input("Cual es el total de deudores diversos: " ))
        funcionario_empleados_balance = float(input("Cual es el total de funcionarios y empleados: "))
        
        producto_terminado_balance = suma_inventario_final_producto
        
        activo_circulante_balance = (efectivo_balance + clientes_balance + deudores_balance + funcionario_empleados_balance + producto_terminado_balance)
        
        print()
        print(f"El activo circulante es de: ${activo_circulante_balance:,}")
        print()
        
        terreno_balance = float(input("Ingrese el valor del terreno: "))
        planta_equipo_balance = float(input("Ingrese el valor de planta y equipo: "))
        maquinaria = compra_activo_fijo
        planta_equipo_total = (planta_equipo_balance + maquinaria)
        
        print()
        print(f"El total de planta y equipo es de: ${planta_equipo_total:,}")
        print()
        
        depreciacion_acomulada = float(input("Cual es la depreciacion acomulada: "))
        depreciacion_tabla_9 = depre
        depreciacion_tabla_8 = depreciacion_9
        depreciacion_acomulada_final = (depreciacion_acomulada - depreciacion_tabla_8 - depreciacion_tabla_9)
        print()
        print(f"La depreciacion acomulada es de: ${depreciacion_acomulada_final:,}")
        print()
        
        total_activos_no_circulantes = (terreno_balance + planta_equipo_total + depreciacion_acomulada_final)
        print()
        print(f"El activo total no circulante es de: ${total_activos_no_circulantes:,}")
        print()
        
        activo_total = (activo_circulante_balance + total_activos_no_circulantes )
        print()
        print(f"El activo total es de: ${activo_total:,}")
        print()
        
        provedores_balance = saldo_proveedores
        documento_pagar = float(input("Cual es la deuda de los documentos: "))
        pagar_isr = impuesto_sobre_renta
        pagar_ptu = reparto_utilidades_empresa
        
        total_pasivo_corto_plazo = (provedores_balance + documento_pagar + pagar_isr + pagar_ptu)
        print()
        print(f"El total de pasivos a corto plazo son de: ${total_pasivo_corto_plazo:,}")
        print()
        
        prestamos_bancarios = float(input("Cuales son los prestamos bancarios de la empresa: "))
        print()
        print(f"El pasivo a largo plazo es de: ${prestamos_bancarios:,}")
        print()
        
        pasivo_total = (total_pasivo_corto_plazo + prestamos_bancarios)
        print()
        print(f"El pasivo total de la empresa es de: ${pasivo_total:,}")
        print()
        
        capital_aportado = float(input("Cuanto capital se aporto: "))
        capital_ganado = float(input("Cual es el capital ganado: "))
        utilidad_neta_ejercicio = utilidad_neta
        
        capital_contable = (capital_aportado + capital_ganado + utilidad_neta_ejercicio)
        print()
        print(f"Total de capital contable es de: ${capital_contable:,}")
        print()
        
        suma_pasivo_capital = (pasivo_total + capital_contable)
        print()
        print(f"La suma de pasivo y capital es de: ${suma_pasivo_capital:,}")
        print()
