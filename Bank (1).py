import streamlit as st

class BankAccount:
    def __init__(self, name, acc_no):
        self.name = name
        self.acc_no = acc_no
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

# Initialize accounts in session_state
if "accounts" not in st.session_state:
    st.session_state.accounts = {}

accounts = st.session_state.accounts

st.title("🏦 Abdullah Bank Management System")

option = st.selectbox(
    "Select Operation",
    (
        "Create Account",
        "Deposit Amount",
        "Withdraw Amount",
        "Check Balance",
        "Delete Account"
    )
)

if option == "Create Account":
    name = st.text_input("Account Holder Name", key="create_name")
    acc_no = st.text_input("Account Number", key="create_acc")

    if st.button("Create Account"):
        if acc_no in accounts:
            st.error("Account already exists")
        else:
            accounts[acc_no] = BankAccount(name, acc_no)
            st.success(f"Account {acc_no} created successfully!")

elif option == "Deposit Amount":
    acc_no = st.text_input("Account Number", key="deposit_acc")
    amount = st.number_input("Amount", min_value=1, key="deposit_amt")

    if st.button("Deposit"):
        if acc_no in accounts:
            accounts[acc_no].deposit(amount)
            st.success("Amount deposited successfully")
        else:
            st.error("Account not found")

elif option == "Withdraw Amount":
    acc_no = st.text_input("Account Number", key="withdraw_acc")
    amount = st.number_input("Amount", min_value=1, key="withdraw_amt")

    if st.button("Withdraw"):
        if acc_no in accounts:
            if accounts[acc_no].withdraw(amount):
                st.success("Withdrawal successful")
            else:
                st.error("Insufficient balance")
        else:
            st.error("Account not found")

elif option == "Check Balance":
    acc_no = st.text_input("Account Number", key="check_acc")

    if st.button("Check Balance"):
        if acc_no in accounts:
            st.info(f"Current Balance: Rs {accounts[acc_no].get_balance()}")
        else:
            st.error("Account not found")

elif option == "Delete Account":
    acc_no = st.text_input("Account Number", key="delete_acc")

    if st.button("Delete Account"):
        if acc_no in accounts:
            del accounts[acc_no]
            st.success("Account deleted successfully")
        else:
            st.error("Account not found")