import ast
import operator as op
import streamlit as st


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Smart Calculator",
    page_icon="🧮",
    layout="centered"
)


# --------------------------------------------------
# Custom CSS
# --------------------------------------------------

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(135deg, #0f172a, #1e293b);
        }

        .main-title {
            text-align: center;
            color: #ffffff;
            font-size: 42px;
            font-weight: 700;
            margin-bottom: 5px;
        }

        .subtitle {
            text-align: center;
            color: #94a3b8;
            margin-bottom: 25px;
        }

        .calculator-box {
            background: #111827;
            padding: 25px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.35);
        }

        div.stButton > button {
            width: 100%;
            height: 55px;
            border-radius: 12px;
            border: none;
            font-size: 20px;
            font-weight: 600;
            background-color: #334155;
            color: white;
            transition: 0.2s;
        }

        div.stButton > button:hover {
            background-color: #475569;
            color: white;
            border: none;
        }

        .operator-button {
            background-color: #f59e0b !important;
        }

        .equal-button {
            background-color: #22c55e !important;
        }

        .clear-button {
            background-color: #ef4444 !important;
        }

        .history-title {
            color: white;
            font-size: 22px;
            font-weight: 600;
            margin-top: 25px;
        }

        .history-item {
            background-color: #1e293b;
            color: #e2e8f0;
            padding: 10px 15px;
            border-radius: 8px;
            margin-bottom: 8px;
        }

        footer {
            visibility: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Safe Calculator
# --------------------------------------------------

OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Mod: op.mod,
    ast.Pow: op.pow,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
}


def safe_calculate(expression):
    """
    Safely evaluate basic mathematical expressions
    without directly exposing eval().
    """

    def evaluate(node):
        if isinstance(node, ast.Expression):
            return evaluate(node.body)

        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Invalid number")

        if isinstance(node, ast.BinOp):
            left = evaluate(node.left)
            right = evaluate(node.right)

            if isinstance(node.op, ast.Div) and right == 0:
                raise ZeroDivisionError("Cannot divide by zero")

            if isinstance(node.op, ast.Pow):
                if abs(right) > 100:
                    raise ValueError("Exponent too large")

            operation = OPERATORS.get(type(node.op))

            if operation is None:
                raise ValueError("Invalid operator")

            return operation(left, right)

        if isinstance(node, ast.UnaryOp):
            operation = OPERATORS.get(type(node.op))

            if operation is None:
                raise ValueError("Invalid operator")

            return operation(evaluate(node.operand))

        raise ValueError("Invalid expression")

    tree = ast.parse(expression, mode="eval")

    return evaluate(tree)


# --------------------------------------------------
# Session State
# --------------------------------------------------

if "expression" not in st.session_state:
    st.session_state.expression = ""

if "history" not in st.session_state:
    st.session_state.history = []


# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🧮 Smart Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Fast, simple and powerful calculator</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# Calculator
# --------------------------------------------------

st.markdown('<div class="calculator-box">', unsafe_allow_html=True)

display = st.text_input(
    "Expression",
    value=st.session_state.expression,
    placeholder="Enter calculation...",
    label_visibility="collapsed"
)

st.session_state.expression = display


# --------------------------------------------------
# Button Helper
# --------------------------------------------------

def add_value(value):
    st.session_state.expression += value


# --------------------------------------------------
# Row 1
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("C", key="clear"):
        st.session_state.expression = ""
        st.rerun()

with col2:
    if st.button("⌫", key="delete"):
        st.session_state.expression = st.session_state.expression[:-1]
        st.rerun()

with col3:
    if st.button("%", key="percent"):
        add_value("%")
        st.rerun()

with col4:
    if st.button("÷", key="divide"):
        add_value("/")
        st.rerun()


# --------------------------------------------------
# Row 2
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("7", key="7"):
        add_value("7")
        st.rerun()

with col2:
    if st.button("8", key="8"):
        add_value("8")
        st.rerun()

with col3:
    if st.button("9", key="9"):
        add_value("9")
        st.rerun()

with col4:
    if st.button("×", key="multiply"):
        add_value("*")
        st.rerun()


# --------------------------------------------------
# Row 3
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("4", key="4"):
        add_value("4")
        st.rerun()

with col2:
    if st.button("5", key="5"):
        add_value("5")
        st.rerun()

with col3:
    if st.button("6", key="6"):
        add_value("6")
        st.rerun()

with col4:
    if st.button("−", key="subtract"):
        add_value("-")
        st.rerun()


# --------------------------------------------------
# Row 4
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("1", key="1"):
        add_value("1")
        st.rerun()

with col2:
    if st.button("2", key="2"):
        add_value("2")
        st.rerun()

with col3:
    if st.button("3", key="3"):
        add_value("3")
        st.rerun()

with col4:
    if st.button("+", key="plus"):
        add_value("+")
        st.rerun()


# --------------------------------------------------
# Row 5
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("0", key="0"):
        add_value("0")
        st.rerun()

with col2:
    if st.button(".", key="decimal"):
        add_value(".")
        st.rerun()

with col3:
    if st.button("(", key="open"):
        add_value("(")
        st.rerun()

with col4:
    if st.button(")", key="close"):
        add_value(")")
        st.rerun()


# --------------------------------------------------
# Calculate Button
# --------------------------------------------------

if st.button("=", key="calculate", use_container_width=True):

    expression = st.session_state.expression.strip()

    if not expression:
        st.warning("Please enter a calculation.")
    else:
        try:
            # Convert percentage into decimal
            expression = expression.replace("%", "/100")

            result = safe_calculate(expression)

            if isinstance(result, float) and result.is_integer():
                result = int(result)

            original_expression = st.session_state.expression

            st.session_state.history.insert(
                0,
                f"{original_expression} = {result}"
            )

            st.session_state.history = st.session_state.history[:10]

            st.session_state.expression = str(result)

            st.rerun()

        except ZeroDivisionError:
            st.error("❌ Cannot divide by zero.")

        except Exception:
            st.error("❌ Invalid calculation. Please check your expression.")


st.markdown("</div>", unsafe_allow_html=True)


# --------------------------------------------------
# History
# --------------------------------------------------

if st.session_state.history:

    st.markdown(
        '<div class="history-title">📜 Calculation History</div>',
        unsafe_allow_html=True
    )

    for item in st.session_state.history:
        st.markdown(
            f'<div class="history-item">{item}</div>',
            unsafe_allow_html=True
        )

    if st.button("Clear History", use_container_width=True):
        st.session_state.history = []
        st.rerun()


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown(
    """
    <br>
    <p style="text-align:center; color:#64748b;">
        Built with Python & Streamlit ❤️
    </p>
    """,
    unsafe_allow_html=True
)
