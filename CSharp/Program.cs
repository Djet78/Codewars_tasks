// See https://aka.ms/new-console-template for more information

try 
{ 
    Console.WriteLine(CreditCardMask.Maskify("1"));
} catch (Exception ex) 
{
    Console.WriteLine(ex.ToString());
} finally 
{
    Console.ReadLine();
}
