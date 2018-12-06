import paintjob, configparser, sys, time

def menu():
    print("\n"*50)
    paintjob.welcome_message()
    print("")
    print("=== Manual Paintjob Configurator ===")
    print("")
    print("1 - View/edit modpack & truck parameters")
    print("")
    print("0 - Exit program")
    print()
    menu_choice = input("Enter selection: ")
    if menu_choice == "1":
        view_params()
    elif menu_choice == "0":
        sys.exit()
    else:
        print("Invalid selection")
        time.sleep(1.5)
        menu() # what was that? recursion? never heard of it

def view_params():
    print("\n"*50)
    list_ini = configparser.ConfigParser()
    list_ini.read("truck lists/manual.ini")
    print("=== Modpack parameters ===")
    print("Mod name:        %s" % list_ini["Params"]["pack_name"])
    print("Mod author:      %s" % list_ini["Params"]["pack_author"])
    print("Mod version:     %s" % list_ini["Params"]["pack_version"])
    print("")
    print("=== In-game paintjob parameters ===")
    print("In-game name:    %s" % list_ini["Params"]["ingame_name"])
    print("Price:           %s" % list_ini["Params"]["price"])
    print("Unlock level:    %s" % list_ini["Params"]["unlock_level"])
    print("")
    print("=== Other parameters ===")
    print("Supported truck: %s" % list_ini["Params"]["database_name"])
    print("Internal name:   %s" % list_ini["Params"]["internal_name"])
    print("")
    print("1 - Edit modpack or in-game parameters")
    print("2 - Edit supported truck")
    print("3 - Edit internal name")
    print("")
    print("0 - Back to previous menu")
    print("")
    menu_choice = input("Enter selection: ")
    if menu_choice == "1":
        edit_params()
    elif menu_choice == "2":
        edit_truck()
    elif menu_choice == "3":
        edit_internal_name()
    elif menu_choice == "0":
        menu()
    else:
        print("Invalid selection")
        time.sleep(1.5)
        view_params

def edit_params():
    print("\n"*50)
    print("Select parameter to edit")
    print("1 - Mod name")
    print("2 - Mod author")
    print("3 - Mod version")
    print("4 - In-game name")
    print("5 - Price")
    print("6 - Unlock level")
    print("")
    print("0 - Back to previous menu")
    print("")
    menu_choice = input("Enter selection: ")
    if menu_choice == "1":
        param_to_edit = ("pack_name", "Mod name")
    elif menu_choice == "2":
        param_to_edit = ("pack_author", "Mod author")
    elif menu_choice == "3":
        param_to_edit = ("pack_version", "Mod version")
    elif menu_choice == "4":
        param_to_edit = ("ingame_name", "In-game name")
    elif menu_choice == "5":
        param_to_edit = ("price", "Price")
    elif menu_choice == "6":
        param_to_edit = ("unlock_level", "Unlock level")
    elif menu_choice == "0":
        param_to_edit = None
        view_params()
    else:
        param_to_edit = None
        print("Invalid selection")
        time.sleep(1.5)
        edit_params()
    if param_to_edit != None:
        print("")
        new_param_value = input("Enter new value for %s: " % param_to_edit[1])
        param_to_edit = param_to_edit[0]
        list_ini = configparser.ConfigParser()
        list_ini.read("truck lists/manual.ini")
        list_ini["Params"][param_to_edit] = new_param_value
        with open("truck lists/manual.ini", "w") as configfile:
            list_ini.write(configfile)
        print("")
        print("Parameter changed successfully")
        time.sleep(2)
        edit_params()

def edit_truck():
    print("\n"*50)
    list_ini = configparser.ConfigParser()
    list_ini.read("truck lists/manual.ini")
    print("Current supported truck: %s" % list_ini["Params"]["database_name"])
    print("")
    print("Make (internal):         %s" % list_ini["Params"]["make"])
    print("Model (internal):        %s" % list_ini["Params"]["model"])
    print("Cabins (internal):       %s" % list_ini["Params"]["cabins"].replace(",", ", "))
    print("")
    print("Select type of truck to support")
    print("1 - Euro Truck Simulator 2")
    print("2 - American Truck Simulator")
    print("3 - Euro Truck Simulator 2 truck mod")
    print("4 - American Truck Simulator truck mod")
    print("5 - Player-owned trailer")
    print("")
    print("0 - Back to previous menu")
    print("")
    menu_choice = input("Enter selection: ")
    vehicle_type = None
    if menu_choice == "1":
        vehicle_type = "euro"
    elif menu_choice == "2":
        vehicle_type = "american"
    elif menu_choice == "3":
        vehicle_type = "euro mod"
    elif menu_choice == "4":
        vehicle_type = "american mod"
    elif menu_choice == "5":
        vehicle_type = "trailer"
    elif menu_choice == "0":
        view_params()
    else:
        print("Invalid selection")
        time.sleep(1.5)
        edit_truck()
    if vehicle_type != None:
        print("\n"*50)
        if vehicle_type == "trailer":
            print("Select trailer to support")
        else:
            print("Select truck to support")
        database_ini = []
        database_ini = configparser.ConfigParser()
        database_ini.read("database.ini")
        vehicles_to_display = []
        for vehicle in database_ini.sections():
            if database_ini[vehicle]["vehicle_type"] == vehicle_type:
                vehicles_to_display.append(vehicle)
        menu_choice_counter = 1
        for vehicle in vehicles_to_display:
            print("%s - %s" % (menu_choice_counter, vehicle))
            menu_choice_counter += 1
        print("")
        menu_choice = input("Enter selection, or nothing to cancel: ")
        database_name = None
        if menu_choice in [str(i+1) for i in range(len(vehicles_to_display))]:
            choose_cabins(vehicles_to_display[int(menu_choice)-1])
        else:
            edit_truck()

def choose_cabins(database_name, cabin_1=False, cabin_2=False, cabin_3=False, cabin_8x4=False):
    print("\n"*50)
    database_ini = []
    database_ini = configparser.ConfigParser()
    database_ini.read("database.ini")
    print("Select cabin of %s to toggle support" % database_name)
    if "cabin_1" in database_ini[database_name]:
        if not cabin_1:
            print("1 - [ ] - %s" % database_ini[database_name]["cabin_1"])
        else:
            print("1 - [X] - %s" % database_ini[database_name]["cabin_1"])
    else:
        cabin_1 = None
    if "cabin_2" in database_ini[database_name]:
        if not cabin_2:
            print("2 - [ ] - %s" % database_ini[database_name]["cabin_2"])
        else:
            print("2 - [X] - %s" % database_ini[database_name]["cabin_2"])
    else:
        cabin_2 = None
    if "cabin_3" in database_ini[database_name]:
        if not cabin_3:
            print("3 - [ ] - %s" % database_ini[database_name]["cabin_3"])
        else:
            print("3 - [X] - %s" % database_ini[database_name]["cabin_3"])
    else:
        cabin_3 = None
    if "cabin_8x4" in database_ini[database_name]:
        if not cabin_8x4:
            print("4 - [ ] - %s" % database_ini[database_name]["cabin_8x4"])
        else:
            print("4 - [X] - %s" % database_ini[database_name]["cabin_8x4"])   ########## UP TO HERE
    else:
        cabin_8x4 = None
    print("")
    print("5 - Confirm")
    print("")
    print("0 - Cancel")
    print("")
    menu_choice = input("Enter selection: ")
    if menu_choice == "1" and cabin_1 != None:
        cabin_1 = not cabin_1
        choose_cabins(database_name, cabin_1, cabin_2, cabin_3, cabin_8x4)
    elif menu_choice == "2" and cabin_2 != None:
        cabin_2 = not cabin_2
        choose_cabins(database_name, cabin_1, cabin_2, cabin_3, cabin_8x4)
    elif menu_choice == "3" and cabin_3 != None:
        cabin_3 = not cabin_3
        choose_cabins(database_name, cabin_1, cabin_2, cabin_3, cabin_8x4)
    elif menu_choice == "4" and cabin_8x4 != None:
        cabin_8x4 = not cabin_8x4
        choose_cabins(database_name, cabin_1, cabin_2, cabin_3, cabin_8x4)
    elif menu_choice == "5" and (cabin_1 or cabin_2 or cabin_3 or cabin_8x4):
        cabins_selected = []
        if cabin_1:
            cabins_selected.append(database_ini[database_name]["cabin_1"])
        if cabin_2:
            cabins_selected.append(database_ini[database_name]["cabin_2"])
        if cabin_3:
            cabins_selected.append(database_ini[database_name]["cabin_3"])
        if cabin_8x4:
            cabins_selected.append(database_ini[database_name]["cabin_8x4"])
        cabins_selected = ",".join(str(i) for i in cabins_selected)
        list_ini = configparser.ConfigParser()
        list_ini.read("truck lists/manual.ini")
        list_ini["Params"]["database_name"] = database_name
        list_ini["Params"]["make"] = database_ini[database_name]["make"]
        list_ini["Params"]["model"] = database_ini[database_name]["model"]
        list_ini["Params"]["cabins"] = cabins_selected
        with open("truck lists/manual.ini", "w") as configfile:
            list_ini.write(configfile)
        print("Supported truck changed successfully")
        time.sleep(1.5)
        edit_truck()
    elif menu_choice == "0":
        edit_truck()
    else:
        print("Invalid selection")
        time.sleep(1.5)
        choose_cabins(database_name, cabin_1, cabin_2, cabin_3, cabin_8x4)

def edit_internal_name():
    pass


menu()