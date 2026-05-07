import streamlit as st
import pandas as pd

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="Advanced Library System", layout="wide")

# ---------------- SESSION STORAGE ----------------
if "books" not in st.session_state:
    st.session_state.books = []

if "issued_books" not in st.session_state:
    st.session_state.issued_books = []

# ---------------- TITLE ----------------
st.title("📚 Advanced Library Management System")

# ---------------- SIDEBAR ----------------
menu = st.sidebar.selectbox(
    "📌 Select Menu",
    [
        "Dashboard",
        "Add Book",
        "View Books",
        "Search Book",
        "Issue Book",
        "Return Book",
        "Delete Book"
    ]
)

# ---------------- DASHBOARD ----------------
if menu == "Dashboard":

    st.header("📊 Dashboard")

    total_books = len(st.session_state.books)
    issued = len(st.session_state.issued_books)
    available = total_books - issued

    col1, col2, col3 = st.columns(3)

    col1.metric("📚 Total Books", total_books)
    col2.metric("✅ Available", available)
    col3.metric("📕 Issued", issued)

    st.divider()

    if st.session_state.books:
        df = pd.DataFrame(st.session_state.books)
        st.subheader("Library Books")
        st.dataframe(df, use_container_width=True)

# ---------------- ADD BOOK ----------------
elif menu == "Add Book":

    st.header("➕ Add New Book")

    title = st.text_input("Book Title")
    author = st.text_input("Author Name")
    category = st.selectbox(
        "Category",
        ["Programming", "Science", "Novel", "History", "Biography"]
    )
    quantity = st.number_input("Quantity", min_value=1, step=1)

    if st.button("Add Book"):

        book = {
            "Title": title,
            "Author": author,
            "Category": category,
            "Quantity": quantity,
            "Status": "Available"
        }

        st.session_state.books.append(book)

        st.success("✅ Book Added Successfully!")

# ---------------- VIEW BOOKS ----------------
elif menu == "View Books":

    st.header("📖 View All Books")

    if st.session_state.books:

        df = pd.DataFrame(st.session_state.books)

        category_filter = st.selectbox(
            "Filter By Category",
            ["All"] + list(df["Category"].unique())
        )

        if category_filter != "All":
            df = df[df["Category"] == category_filter]

        st.dataframe(df, use_container_width=True)

    else:
        st.warning("⚠ No books available")

# ---------------- SEARCH BOOK ----------------
elif menu == "Search Book":

    st.header("🔍 Search Book")

    search = st.text_input("Enter Book Title")

    if search:

        results = []

        for book in st.session_state.books:
            if search.lower() in book["Title"].lower():
                results.append(book)

        if results:
            st.success("Book Found ✅")
            st.dataframe(pd.DataFrame(results), use_container_width=True)
        else:
            st.error("❌ No Book Found")

# ---------------- ISSUE BOOK ----------------
elif menu == "Issue Book":

    st.header("📤 Issue Book")

    if st.session_state.books:

        titles = [book["Title"] for book in st.session_state.books]

        selected_book = st.selectbox("Select Book", titles)

        student = st.text_input("Student Name")

        if st.button("Issue"):

            for book in st.session_state.books:

                if book["Title"] == selected_book:

                    if book["Status"] == "Available":

                        book["Status"] = "Issued"

                        issue_data = {
                            "Book": selected_book,
                            "Student": student
                        }

                        st.session_state.issued_books.append(issue_data)

                        st.success("📕 Book Issued Successfully")

                    else:
                        st.error("Book Already Issued")

    else:
        st.warning("No Books Available")

# ---------------- RETURN BOOK ----------------
elif menu == "Return Book":

    st.header("📥 Return Book")

    if st.session_state.issued_books:

        issued_titles = [
            item["Book"]
            for item in st.session_state.issued_books
        ]

        return_book = st.selectbox(
            "Select Book To Return",
            issued_titles
        )

        if st.button("Return Book"):

            for book in st.session_state.books:

                if book["Title"] == return_book:
                    book["Status"] = "Available"

            st.session_state.issued_books = [
                item
                for item in st.session_state.issued_books
                if item["Book"] != return_book
            ]

            st.success("✅ Book Returned Successfully")

    else:
        st.info("No Issued Books")

# ---------------- DELETE BOOK ----------------
elif menu == "Delete Book":

    st.header("❌ Delete Book")

    if st.session_state.books:

        titles = [book["Title"] for book in st.session_state.books]

        delete_book = st.selectbox(
            "Select Book",
            titles
        )

        if st.button("Delete"):

            st.session_state.books = [
                book
                for book in st.session_state.books
                if book["Title"] != delete_book
            ]

            st.success("🗑 Book Deleted Successfully")

    else:
        st.warning("No Books Available")