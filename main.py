import sklearn
import pickle
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

global info
info = {}
info["sex"] = 1
global data
data = []
global result
result = None


class HeartApp(MDApp):


        def build(self):
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Red"
            # self.theme_cls.accent_color ="Lime"
            
            return Builder.load_file('app.kv')


        def get_state(self, widget):

            if widget.state == "down":
                widget.text = "Yes"
            else:
                widget.text = "No"

        def get_gender(self, instance, value, gender):
            global sex
            sex = 1
            if value:
                if gender == "female":
                    sex = 0
                else:
                    sex = 1
            else:
                info["sex"] = 1

            info["sex"] = sex

        def get_data(self):
            data = []
            self.dialog =None
            try:
                convert = {"No": 0, "Yes": 1}
                age = int(self.root.ids.my_age.text)

                data.append(age)
                anaemia = convert[self.root.ids.anaemia.text]
                data.append(anaemia)
                creatinine_phospho = float(self.root.ids.creatinine_phospho.text)

                data.append(creatinine_phospho)
                diabetes = convert[self.root.ids.diabetes.text]
                data.append(diabetes)
                ejec_fra = float(self.root.ids.ejection_fraction.text)

                data.append(ejec_fra)
                h_b_p = convert[self.root.ids.high_blood_pressure.text]
                data.append(h_b_p)
                p = int(self.root.ids.platelets.text)

                data.append(p)
                sc = float(self.root.ids.serum_creatinine.text)

                data.append(sc)
                ss = float(self.root.ids.serum_sodium.text)

                data.append(ss)
                sex = info["sex"]
                data.append(sex)
                smoking = convert[self.root.ids.smoking.text]
                data.append(smoking)
                return data
            except:
                return 0


        def close(self, obj):
            self.dialog.dismiss()
            self.dialog = None





        def predict(self):
                d = self.get_data()
                if d==0:
                    self.dialog = MDDialog(
                        title="data is missing",
                        buttons=[
                            MDFlatButton(text="OK", on_release=self.close)
                        ]
                    )
                else :
                    with open("model.pkl", "rb") as f:
                        model = pickle.load(f)
                    res = model.predict([d])[0]
                    d.clear()
                    if self.dialog is None :

                        if res == 0:
                            result_text = "the heart is healthy"
                        else:
                            result_text = "the heart is unhealthy"
                        self.dialog = MDDialog(
                            title="Get your result",
                            text=result_text,

                            buttons=[
                                MDFlatButton(text="OK", on_release=self.close)
                            ]
                        )
                        self.dialog.open()

                   

        def display(self):
                    self.wait()
                    self.predict()


HeartApp().run()
