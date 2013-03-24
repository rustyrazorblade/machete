## -*- coding: utf-8 -*-
<%inherit file="/base.mako"/>

<%block name="metatitle">Projects | ${parent.metatitle()}</%block>

<%block name="content">
    <div class="container">
        <div class="span10">
        <a href="/projects/${project.vid}">Back</a>
        <form id="create_issue" action="/projects/${project.vid}/issues/" method="POST">
            <input type="hidden" id="project" value="${project.vid}"/>
            <fieldset>
                <legend>Create an Issue</legend>
                <label>Name</label>
                <input type="text" size=80, placeholder="Give a descriptive name…" name="name"/>
                <span class="help-block">This will show up in people's issue lists.</span>

                <label>Severity</label>
                <select name="severity">
                    %for sev in project.severities:
                        <option value="${sev.id}">${sev.name}</option>
                    %endfor
                </select>

                <label type="text" >Description</label>
                <textarea rows=15 name="description"></textarea>

                <!-- <label type="text">Severity</label> -->
            <input type="submit" value="Create" />

        </form>
        </div>
    </div>
</%block>
