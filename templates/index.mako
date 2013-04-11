## -*- coding: utf-8 -*-
<%inherit file="/base.mako"/>

<%block name="metatitle">Home | ${parent.metatitle()}</%block>

<%block name="content">
    <div class="container">
        <div class="row">
            <div class="span8">
                <h3>Questions</h3>
                    <table class="table table-striped">
                        <tr>
                            <td>Who is jon haddad? In regards to Issue #52</td>
                        </tr>
                    </table>
                    <a>More questions...</a>

                <h3>Issues</h3>
                <table class="table table-striped">
                    <tr>
                        <td>Some issue</td>
                    </tr>
                    <tr>
                        <td>Some other issue</td>
                    </tr>
                </table>

                <a>See all issues...</a>
            </div>

            <div class="span4">
                <h3>Projects</h3>
                <table class="table table-striped">
                        % for p in session.user.projects:
                            <tr>
                                <td><a href="/projects/${p.vid}">${p.name}</a></td>
                            </tr>
                        % endfor
                </table>

            </div>

    </div>
</%block>
