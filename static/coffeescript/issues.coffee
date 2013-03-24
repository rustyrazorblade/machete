$ ->
  $("#create_issue").submit ->
    $.post this.action, $(this).serialize(), (response) ->
        issue = response.data

    return false

