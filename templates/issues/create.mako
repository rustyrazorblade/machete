## -*- coding: utf-8 -*-
<%inherit file="/base.mako"/>

<%block name="metatitle">Projects | ${parent.metatitle()}</%block>

<%block name="content">
    <div class="container">
        <a href="/projects/${project.vid}">Back</a>
        <h1>Create an issue</h1>
        <form id="create_issue">
            <fieldset>
                <legend>Create an Issue</legend>
                <label>Name</label>
                <input type="text" size=30, placeholder="Give a descriptive name…" />
                <span class="help-block">This will show up in people's issue lists.</span>
                <label type="text">Description</label>
                <textarea rows=15></textarea>
                <label type="text">Severity</label>

        </form>
    </div>
</%block>
