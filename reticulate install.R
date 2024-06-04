# instala o pacote reticulate no R
install.packages("reticulate")

# Carregue o reticulate
library("reticulate")

## Instala o Miniconda manualmente
install_miniconda()

# Cria o ambiente virtual r-reticulate (rodar uma única vez)
conda_create("r-reticulate", packages = c("numpy", "pandas"))

# Ativa o ambiente chamado r-reticulate (rodar a cada nova sessão)
use_condaenv("r-reticulate", required = TRUE)

# Verifica as configurações do ambiente (versão do Python, pacotes, etc)
py_discover_config()
