$ ->
  $("#create_issue").submit ->
    $.post this.action, $(this).serialize(), (response) ->
        issue = response.data
        document.location.href = "/projects/#{issue.project.id}/issues/#{issue.id}"

    return false

