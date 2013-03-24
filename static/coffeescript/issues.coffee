$ ->
  $("#create_issue").submit ->
    $.post this.action, $(this).serialize(), (response) ->
        issue = response.data
        document.location.href = "/projects/#{issue.project_id}/issues/#{issue.id}"

    return false

