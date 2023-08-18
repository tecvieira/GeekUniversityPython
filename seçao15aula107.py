def seja_educado_mesmo(funcao): # Decorators Functions
    def sendo_mesmo():
        print('Foi um prazer conhecer voce')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo


@seja_educado_mesmo # Decorators forma pythonica de aplicar
def apresentando():
    print('Meu nome é Pedro')


apresentando()