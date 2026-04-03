from __future__ import annotations

from flask import Flask, abort, render_template, request

from bc_portal.services import SERVICE_MODULES, get_dashboard_cards, get_service_module


def _build_form_state(fields: list[dict], form_data) -> dict:
    values = {}
    for field in fields:
        name = field["name"]
        field_type = field.get("type", "text")
        if field_type == "checkbox":
            values[name] = name in form_data if form_data else bool(field.get("default", False))
            continue
        if not form_data:
            values[name] = field.get("default", "")
            continue
        submitted_value = form_data.get(name, field.get("default", ""))
        if field_type == "number":
            try:
                values[name] = int(submitted_value)
            except (TypeError, ValueError):
                values[name] = int(field.get("default", 0))
        else:
            values[name] = submitted_value
    return values


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def dashboard():
        return render_template(
            "dashboard.html",
            cards=get_dashboard_cards(),
            total_services=len(SERVICE_MODULES),
        )

    @app.route("/services/<slug>", methods=["GET", "POST"])
    def service_detail(slug: str):
        service_module = get_service_module(slug)
        if service_module is None:
            abort(404)

        form_state = _build_form_state(service_module.FORM_FIELDS, request.form)
        result = service_module.build_response(form_state)

        return render_template(
            "service.html",
            card=service_module.SERVICE_CARD,
            challenge=service_module.BUILDER_CHALLENGE,
            fields=service_module.FORM_FIELDS,
            form_state=form_state,
            result=result,
        )

    return app
