def primeros_auxilios():
    print("Iniciando protocolo de primeros auxilios...")

    respuesta_estimulos = input("¿Responde a Estímulos? (Si/No): ").strip().lower()

    if respuesta_estimulos == "si":
        print("Valorar la necesidad de llevarlo al hospital más cercano.")
    elif respuesta_estimulos == "no":
        print("Abrir la vía Aérea.")
        
        while True: 
            respira = input("¿Respira? (Si/No): ").strip().lower()

            if respira == "si":
                print("Permitirle posición de suficiente ventilación.")
        
                break 

            elif respira == "no":
                print("Administrar 5 Ventilaciones y llamar a Ambulancia.")
                
                while True: 
                    signos_vida = input("¿Tiene Signos de Vida? (Si/No): ").strip().lower()

                    if signos_vida == "si":
                        print("Reevaluar a la espera de la Ambulancia.")
                       
                        llego_ambulancia = input("¿Llegó la Ambulancia? (Si/No): ").strip().lower()
                        if llego_ambulancia == "si":
                            print("Fin del protocolo.")
                            return
                        elif llego_ambulancia == "no":
                           
                            pass 
                        else:
                            print("Respuesta no válida. Por favor, responde 'Si' o 'No'.")
                            continue 

                    elif signos_vida == "no":
                        llego_ambulancia = input("¿Llegó la Ambulancia? (Si/No): ").strip().lower()
                        if llego_ambulancia == "no":
                            print("Administrar Compresiones Torácicas hasta que llegue ambulancia.")
                           
                            pass 
                        elif llego_ambulancia == "si":
                            print("Fin del protocolo.")
                            return 
                        else:
                            print("Respuesta no válida. Por favor, responde 'Si' o 'No'.")
                            continue 
                    else:
                        print("Respuesta no válida. Por favor, responde 'Si' o 'No'.")
                        continue 
            else:
                print("Respuesta no válida. Por favor, responde 'Si' o 'No'.")
                continue 

    else:
        print("Respuesta no válida. Por favor, responde 'Si' o 'No'.")

    print("Fin del protocolo.") 

if __name__ == "__main__":
    primeros_auxilios()