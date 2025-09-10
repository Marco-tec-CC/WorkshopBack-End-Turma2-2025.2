import requests
from django.shortcuts import render
from .forms import ViaCepForm
from .models import ViaCep
from django.views.generic import FormView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy


class ViaCepForm(FormView):
    template_name = ViaCepForm
    success_url = reverse_lazy

    def form_valid(self, form):
        cep = form.cleaned_data['cep'].replace('-','').strip() 
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                #salvar ou atualizar no banco
                cep_obj, created = ViaCep.objects.update_or_create(
                    cep=cep,
                    defaults={
                        "logradouro": data.get("logradouro", ""),
                        "bairro": data.get("bairro", ""),
                        "localidade": data.get("localidade", ""),
                        "uf": data.get("uf", ""),
                    },
                )
                self.object = cep_obj
            else:
                form.add_error("cep", "CEP não encontrado na API do ViaCEP.")
                return self.form_invalid(form)
        
        else:
            form.add_error("cep", "erro ao consultar a API do ViaCEP.")
            return self.form_invalid(form)
        
        return super().form_valid(form)
    
    class ViaCepListView(ListView):
        model = ViaCep
        template_name = "viacep/viacep_detail.html"
        context_object_name = "ceps"
    
    class ViaCepDetailView(DetailView):
        model = ViaCep 
        template_name = "viacep/viacep_detail.html"
        context_object_name = "cep"

    class ViaCepDeleteView(DeleteView):
        model = ViaCep
        template_name = "viacep/viacep_delete.html"
        context_object_name = reverse_lazy

    class ViacepformView(FormView):
        model = ViaCep
        template_name = "viacep/viacep_form.html"
        context_object_name = reverse_lazy
            