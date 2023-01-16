resource "local_file" "kebab" {
    content = ""
  filename = each.value
  for_each = toset(var.filename)
}