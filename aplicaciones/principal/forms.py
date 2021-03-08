from .models import Usuarios, Cuenta, Retiro, Depositos, Transferencia, HistorialTransferencia
from django import forms



class RegistroForm(forms.ModelForm):

    class Meta:
        model = Usuarios
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.TextInput(
                attrs = {
                    'type': "date",
                }
            ),
            'contraseña': forms.PasswordInput(
                attrs={
                'type': 'password',
                }
            ), 
            'contraseña_val': forms.PasswordInput(
                attrs={
                'type': 'password',
                }
            ), 
        }

class CuentaForm(forms.ModelForm):
    
    class Meta:
        model = Cuenta
        fields = [
                    "num_cuenta",  
                    "fondos", 
                 ]  
        labels = {
                    'num_cuenta': 'Numero de Cuenta',
                    'fondos': 'Fondo',
        }

class RetiroForm(forms.ModelForm):
    
    class Meta:
        model = Retiro
        fields = [
                    "num_cuenta",  
                    "banco", 
                    "monto",  
                    "nomtitular",
                 ]  
        labels = {
                    'num_cuenta': 'Numero de Cuenta',  
                    'banco': 'Tipo de Banco',
                    'monto': 'Monto',
                    'nomtitular': 'Nombre de Titular',
        }
        banco = (('bcp','BCP'),('interbank','Interbank'),('bbva','BBVA'),('scotiabank','SCOTIABANK'))
        
        widgets = {
           
            'banco': forms.RadioSelect(choices=banco,attrs={
                
             }),
            'monto': forms.NumberInput(attrs={'min': '0'}), 
        }            

class DepositoForm(forms.ModelForm):
    
    class Meta:
        model = Depositos
        fields = [
                    "monto",  
                    "banco", 
                    "num_cuenta",  
                    "nomtitular", 
                 ]  
        labels = {
                    'monto': 'Monto',  
                    'banco': 'Tipo de Banco', 
                    'num_cuenta': 'Numero de Cuenta',
                    'nomtitular': 'Nombre de Titular',
        }
        
        banco = (('bcp','BCP'),('interbank','Interbank'),('bbva','BBVA'),('scotiabank','SCOTIABANK'))
        
        widgets = {
           
            'banco': forms.RadioSelect(choices=banco,attrs={
                
             }),
            'monto': forms.NumberInput(attrs={'min': '0'}), 
        }


class TransForms(forms.ModelForm):
    class Meta:
        model = Transferencia
        fields = ('num_cuenta','nom_cuenta', 'dni','monto', 'validacion','tipo_trans')
        # widgets = {
        #     'num_cuenta': forms.Select(attrs={
        #         # 'disabled': True,
        #         # 'style': "display:none"
                
        #          }),
        #     'nom_cuenta': forms.TextInput(attrs={
        #         'style': "width:100%, border:5px",
        #         'type': 'date',
        #     })
        #     # 'num_cuenta': forms.HiddenInput(),
        # }
# class UsuariosForms(forms.ModelForm):
#     class Meta:
#          model = Usuarios
#          fields = '__all__'


    '''Registro   labels = {  'nombre': 'Nombre:' ,
                    'apellido': 'Apellidos:' , 
                    'sexo': 'Sexo:' , 
                    'fchnaci': 'Fecha de Nacimiento:', 
                    'correo': 'Correo Electronico:', 
                    'contraseña': 'Contraseña:',
                    'contraseraval': 'Confirmar Contraseña:' ,
                    'condicionesval': 'Acepto Terminos y Condiciones:',
                    'tipo_documento': 'Tipo de Documento:' ,
                    'nro_documento': 'Nro. de Documento:' ,
                    'telefono': 'Teléfono:' ,
                    'dirrecion': 'Dirección:',
                    'nro_cuenta': 'Numero de Cuenta:',
        }
        Genero=[('M','Masculino'),('F','Femenino'),('NE','No especificar')]
        TipoDocumento=[('DNI','Documento de Identidad'),('VISA','Visa de Extranjeria'),('Pasaporte','Pasaporte')]   
        widgets = {
            'nombre': forms.TextInput(attrs={
                'style': "width:30%",
                }),
            'apellido': forms.TextInput(attrs={
                'style': "width:30%",
                }),
            'sexo': forms.RadioSelect(choices=Genero,attrs={
                'style': 'style-list:none',
                }),
            'fchnaci': forms.DateInput(attrs={
                'type': 'date',
                }),
            'correo': forms.EmailInput(attrs={
                'type': 'email',
                'style': "width:30%",
                }),
            'contraseña': forms.PasswordInput(attrs={
                'type': 'password',
                'style': "width:20%",
                }), 
            'contraseraval': forms.PasswordInput(attrs={
                'type': 'password',
                'style': "width:20%",
                }), 
            'tipo_documento': forms.Select(choices=TipoDocumento,attrs={
                }),
            'nro_documento': forms.TextInput(attrs={
                'style': "width:30%",
                }),
            'telefono': forms.TextInput(attrs={
                'style': "width:30%",
                }),
            'dirrecion': forms.TextInput(attrs={
                'style': "width:30%",
                }),
            'nro_cuenta': forms.TextInput(attrs={
                'style': "width:30%",
                }),
            'condicionesval': forms.CheckboxInput(attrs={
                'type': 'checkbox',
                 }),
  }
'''