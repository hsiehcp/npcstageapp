import streamlit as st

# Function to get the nasopharyngeal cancer stage based on TNM values
def get_nasopharyngeal_cancer_stage(T, N, M):
    if M == "M1":
        return "Stage IVC"
    elif N == "N3" or (T == "T4" and N in ["N0", "N1", "N2"]):
        return "Stage IVB"
    elif (T in ["T3"] and N in ["N0", "N1", "N2"]) or (T in ["T1", "T2"] and N == "N2"):
        return "Stage III"
    elif T in ["T1", "T2"] and N in ["N0", "N1"]:
        return "Stage II"
    elif T == "T1" and N == "N0":
        return "Stage I"
    elif T == "Tis" and N == "N0":
        return "Stage 0"
    else:
        return "Stage not defined for given inputs."

# Function to display the AJCC TNM Classification and Staging from a markdown file
def display_ajcc_tnm_and_stage():
    try:
        with open('AJCCNPC.mkd', 'r') as file:
            content = file.read()
            st.markdown(content)
    except FileNotFoundError:
        st.error("AJCCNPC.mkd file not found. Please ensure the file is in the correct location.")

# Streamlit app main function
def main():
    st.title("Nasopharyngeal Cancer Staging")

    # Display the AJCC TNM Classification and Staging
    display_ajcc_tnm_and_stage()

    # Input fields for T, N, M values
    T = st.selectbox("Enter the T value", ["T1", "T2", "T3", "T4", "TX", "T0", "Tis"])
    N = st.selectbox("Enter the N value", ["N0", "N1", "N2", "N3", "NX"])
    M = st.selectbox("Enter the M value", ["M0", "M1"])

    # Button to calculate stage
    if st.button("Get Cancer Stage"):
        stage = get_nasopharyngeal_cancer_stage(T, N, M)
        st.success(f"The nasopharyngeal cancer stage is: {stage}")

if __name__ == "__main__":
    main()

