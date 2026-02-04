import os
import streamlit.components.v1 as components

# Build path to frontend
_parent_dir = os.path.dirname(os.path.abspath(__file__))
_build_dir = os.path.join(_parent_dir, "frontend")

_component_func = components.declare_component(
    "qr_scanner",
    path=_build_dir,
)

def qr_scanner(key=None):
    """Render a continuous QR scanner using html5-qrcode (client-side)."""
    return _component_func(key=key)