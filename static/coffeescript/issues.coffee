$ ->
  $("#create_issue").submit ->
    $.post this.action, $(this).serialize(), (response) ->
        alert "hi"

    return false

