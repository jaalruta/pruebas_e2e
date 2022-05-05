describe ('crear', function(){
    it ('login', function(){
        cy.visit("http://localhost:2368/ghost/#/signin");
        cy.get('#ember7').type('j.otalvaro@uniandes.edu.co');
        cy.get('#ember9').type('irchete7811');
        cy.get('#ember11 > span').click();
        cy.get('.ember-view.gh-secondary-action.gh-nav-new-post').click();
        cy.get('.gh-editor-title.ember-text-area.gh-input.ember-view').type('POST DE PRUEBA');
        cy.get('.koenig-editor__editor.__mobiledoc-editor.__has-no-content').type("PRUEBAS AUTOMATIZADAS MISO");
        cy.get('#ember67 > span').click();
        cy.get('#ember75 > span').click();
        cy.get('#ember77 > span').click();
    })
})