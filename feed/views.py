from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

class ExpensesPageView(TemplateView):
    template_name = "expenses.html"

class FundsPageView(TemplateView):
    template_name = "funds.html"

class ProjectionsPageView(TemplateView):
    template_name = "projections.html"

class TargetsPageView(TemplateView):
    template_name = "targets.html"
