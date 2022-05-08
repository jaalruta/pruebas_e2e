describe ('editar staff', function(){
    beforeEach(() => {
        cy.visit('http://localhost:2368/ghost')
        cy.wait(5000)
      })

    it ('editar staff', function(){
        cy.visit("http://localhost:2368/ghost/#/signin");
        cy.get('#ember7').type(Cypress.config('usuario'));
        cy.get('#ember9').type(Cypress.config('pass'));
        cy.get('#ember11').click();
        cy.wait(5000);
        cy.get(".gh-nav-body a[href='#/settings/']").click();
        cy.wait(2000);

        cy.get(".view-container a[href='#/settings/staff/']").click();
        cy.wait(2000);

        cy.get(".apps-card-app").click();

        cy.get('#user-name').type('{selectall}{backspace}pruebas staff edicion cypress');
        cy.get('#user-bio').type('{selectall}{backspace}nota de prueba edicion cypress');

        cy.get(".view-actions button.gh-btn-primary").click();

        cy.get('#user-name').should('have.value', 'pruebas staff edicion cypress');


    })
})