class CarsList:
    def read_makes(self):
        """Reads the car_makes file and returns a list of makes"""

        with open("/car_info/car_makes.txt", 'r')
        as car_makes:
            make_list = car_makes.readlines()
            for i, make in enumerate(make_list):
                make_list[i] = make.strip()

        return make_list


    def read_models(self):
        """Reads the car models file and returns a list of car models"""

        with open("/car_info/car_models.txt", 'r')
        as car_models:
            model_list = car_models.readlines()
            for i, model in enumerate(model_list):
                model_list[i] = model.strip()

        return model_list

    def create_dictionary(self):
        """Envokes read_makes and read_models methods and produces a dictionary of car makes and models."""

        makes = self.read_makes()
        models = self.read_models()

        makes_models = dict()
        for make in makes:
            makes_models[make] = []

        for model in models:
            for make in makes_models.keys():
                if make.startswith(model[0]):
                    makes_models[make].append(model[2:])

        return makes_models

cars = CarsList()

print(cars.create_dictionary())

