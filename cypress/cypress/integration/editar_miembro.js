describe ('editar', function(){
    beforeEach(() => {
        cy.visit('http://localhost:2368/ghost')
        cy.wait(5000)
      })
    it ('login', function(){
        cy.visit("http://localhost:2368/ghost/#/signin");
        cy.get('#ember7').type(Cypress.config('usuario'));
        cy.get('#ember9').type(Cypress.config('pass'));
        cy.get('#ember11').click();
        cy.wait(2000);
        cy.get(".gh-nav-body a[href='#/members/']").click();
        cy.wait(1000);
        cy.get(".gh-canvas-header a[href='#/members/new/']").click();
        cy.wait(1000);
        cy.get('.gh-cp-member-email-name.ember-text-field.gh-input.ember-view.member-name').type("miembro333"); 
        cy.wait(2000);
        cy.get('#member-email').type("pruebas333@ghost.com");
        cy.wait(2000);
        cy.get('#member-note').type("Esta es una nota de prueba");
        cy.wait(2000);
        cy.get(".view-actions button.gh-btn-primary").click();
        cy.wait(1000);
        cy.get(".gh-nav-body a[href='#/members/']").click();
        cy.wait(1000);
        cy.get(".gh-main tr:nth-child(2) a:nth-child(1)").click();
        cy.wait(1000);
        cy.get('.gh-cp-member-email-name.ember-text-field.gh-input.ember-view.member-name').type("miembroedicion");
        cy.wait(2000);
        cy.get('#member-email').type("pruebasedicion@ghost.com");
        cy.wait(2000);
        cy.get('#member-note').type("Esta es una nota de edicion");
        cy.wait(2000);
        cy.get(".view-actions button.gh-btn-primary").click();
        cy.wait(1000);
        cy.get(".gh-nav-body a[href='#/members/']").click();
        cy.wait(1000);
    })
})