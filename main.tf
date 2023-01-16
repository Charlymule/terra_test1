resource "local_file" "kebab" {
    content = ""
  files = each.value
  for_each = toset(var.filename)
}