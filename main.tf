resource "local_file" "recette_kebab" {
    content = ""
  files = each.value
  for_each = toset(var.filename)
}
