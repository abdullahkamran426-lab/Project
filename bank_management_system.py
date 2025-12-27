
import streamlit as st

class BankAccount:
    def __init__(self, name, account_no):
        self.name = name
        self.account_no = account_no
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


accounts = {}

st.title("🏦 Bank Management System")
st.write("Using OOP and Streamlit")

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
    st.subheader("Create Account")
    name = st.text_input("Account Holder Name")
    acc_no = st.text_input("Account Number")

    if st.button("Create"):
        if acc_no in accounts:
            st.error("Account already exists")
        else:
            accounts[acc_no] = BankAccount(name, acc_no)
            st.success("Account created successfully")

elif option == "Deposit Amount":
    st.subheader("Deposit Money")
    acc_no = st.text_input("Account Number")
    amount = st.number_input("Enter Amount", min_value=1)

    if st.button("Deposit"):
        if acc_no in accounts:
            accounts[acc_no].deposit(amount)
            st.success("Amount deposited successfully")
        else:
            st.error("Account not found")

elif option == "Withdraw Amount":
    st.subheader("Withdraw Money")
    acc_no = st.text_input("Account Number")
    amount = st.number_input("Enter Amount", min_value=1)

    if st.button("Withdraw"):
        if acc_no in accounts:
            if accounts[acc_no].withdraw(amount):
                st.success("Withdrawal successful")
            else:
                st.error("Insufficient balance")
        else:
            st.error("Account not found")

elif option == "Check Balance":
    st.subheader("Check Balance")
    acc_no = st.text_input("Account Number")

    if st.button("Check"):
        if acc_no in accounts:
            st.info(f"Current Balance: Rs {accounts[acc_no].get_balance()}")
        else:
            st.error("Account not found")

elif option == "Delete Account":
    st.subheader("Delete Account")
    acc_no = st.text_input("Account Number")

    if st.button("Delete"):
        if acc_no in accounts:
            del accounts[acc_no]
            st.success("Account deleted successfully")
        else:
            st.error("Account not found")
