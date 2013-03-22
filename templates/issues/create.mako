## -*- coding: utf-8 -*-
<%inherit file="/base.mako"/>

<%block name="metatitle">Projects | ${parent.metatitle()}</%block>

<%block name="content">
    <div class="container">
        <div class="span10">
        <a href="/projects/${project.vid}">Back</a>
        <form id="create_issue" action="#" method="POST">
            <fieldset>
                <legend>Create an Issue</legend>
                <label>Name</label>
                <input type="text" size=80, placeholder="Give a descriptive name…" />
                <span class="help-block">This will show up in people's issue lists.</span>

                <label type="text">Description</label>
                <textarea rows=15></textarea>

                <label type="text">Severity</label>
            <input type="submit" value="Create" />

        </form>
        </div>
    </div>
</%block>
