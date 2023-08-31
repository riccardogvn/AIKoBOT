mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"riccardogiovanelli.mail@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
\n\
[theme]\n\
base = \"light\"\n\
primaryColor = \"#DBBEB4\"\n\
backgroundColor = \"#DBD1B4\"\n\
secondaryBackgroundColor = \"#D2DBB4\"\n\
textColor = \"#000000\"\n\
font = \"sans serif\"\n\
" > ~/.streamlit/config.toml
