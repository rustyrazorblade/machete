## -*- coding: utf-8 -*-
<%inherit file="/base.mako"/>

<%block name="metatitle">Projects | ${parent.metatitle()}</%block>

<%block name="content">
    <div class="container">
        <h1>Issues</h1>
        <a class="btn" href="/projects/${project.vid}/issues/create">Create issue</a>
        <table>
        % for issue in issues:
            <tr>
                <td><a href="/projects/${project.vid}/issues/${issue.vid}">${issue.name}</a></td>
            </tr>
        % endfor
        </table>

        <h1>Wiki</h1>
        <a href="/projects/${project.vid}/wiki/">Go to wiki</a>
        <table>

        </table>
    </div>
</%block>
