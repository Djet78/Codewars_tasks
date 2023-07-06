// See https://aka.ms/new-console-template for more information

try 
{ 
    // Console.WriteLine(CreditCardMask.Maskify("1"));
    Console.WriteLine(EnoughSpace.Enough_(100, 20, 50));
} catch (Exception ex) 
{
    Console.WriteLine(ex.ToString());
} finally 
{
    Console.ReadLine();
}
