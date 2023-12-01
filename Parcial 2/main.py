from Controller.ControllerPaciente import ControllerPaciente
def exec():
    loop = True

    while loop == True:
        controller = ControllerPaciente()
        option = controller.menu()
        controller.listar_pacientes()
        if option == "1":
            controller.mostrar_mayores()
        elif option == "2":
            controller.seleccionar_paciente()
            controller.cambiar_peso()
        elif option == "3":
            controller.seleccionar_paciente()
            controller.peso_sano()
        elif option == "4":
            controller.seleccionar_paciente()
            controller.diferencia_peso()


if __name__ == '__main__':
    exec()