describe ('login', function(){
    it ('login', function(){
        cy.visit("http://localhost:2368/ghost/#/signin");
        cy.get('#ember7').type('j.otalvaro@uniandes.edu.co');
        cy.get('#ember9').type('irchete7811');
        cy.get('#ember11 > span').click();
    })
})