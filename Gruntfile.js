
module.exports = function(grunt) {

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        coffee: {
            compile: {
                files: {
                        'static/js/machete.js': ['static/coffeescript/*.coffee'] // compile and concat into single file
                }
            }
        },
        watch: {
            scripts: {
                files: ["static/coffeescript/*.coffee"],
                tasks: ["coffee"],
                options: {
                    nospawn: true
                }
            }
        }

    });

    // Load the plugin that provides the "uglify" task.
    //grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-coffee');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Default task(s).
    //grunt.registerTask('default', ['uglify']);

};
