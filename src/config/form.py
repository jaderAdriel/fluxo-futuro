from django import forms


class BaseStyledForm(forms.ModelForm):
    """
    Adiciona automaticamente:
    - class="form-control"
    - class="is-invalid" em campos com erro
    - mantém attrs existentes
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            widget = field.widget
            css = widget.attrs.get("class", "")

            css += " form-control"

            # aplica is-invalid se houver erro
            if name in self.errors:
                css += " is-invalid"

            widget.attrs["class"] = css.strip()