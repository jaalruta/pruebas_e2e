describe ('login', function(){
    it ('login', function(){
        cy.visit("http://localhost:2368/ghost/#/signin");
        cy.get('#ember7').type('j.otalvaro@uniandes.edu.co');
        cy.wait(1000);
        cy.get('#ember9').type('irchete7811');
        cy.wait(1000);
        cy.get('#ember11 > span').click();
        cy.wait(1000);
        cy.get('.ember-view.gh-secondary-action.gh-nav-new-post').click();
        cy.wait(1000);
        cy.get('.gh-editor-title.ember-text-area.gh-input.ember-view').type('POST DE PRUEBA PROGRAMADO');
        cy.wait(2000);
        cy.get('.koenig-editor__editor').type("PRUEBAS AUTOMATIZADAS MISO");
        cy.wait(2000);
        cy.get('.ember-view.ember-basic-dropdown-trigger.gh-btn.gh-btn-editor.gh-publishmenu-trigger').click();
        cy.wait(1000);
        cy.get('.gh-date-time-picker').click();
        cy.get('.gh-publishmenu-button').click();
        cy.get('.gh-btn.gh-btn-black.gh-btn-icon.ember-view').click();
        cy.get('.ember-view.gh-editor-back-button').click();

    })
})