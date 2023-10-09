if req.method == 'POST':
        mi_formulario = ClubesFormulario (req.POST)
        if mi_formulario.is_valid():
            data= mi_formulario.cleaned_data
            equipo = Clubes (Nombre=data['Nombre'], Ciudad=data['Ciudad'], Provincia=data['Provincia'], Categoria=data['Categoria'])
            equipo.save()
            return HttpResponse (f'{equipo.Nombre} creado exitosamente')
    else:
        mi_formulario = ClubesFormulario ()
        return render (req, "clubes_formularios.html", {'mi_formulario': mi_formulario})